import os.path

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

from git import Repo
from git.exc import NoSuchPathError

from lint_computer.core import reporters


class GithubOrganization(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    github_id = models.IntegerField(null=True, blank=True)
    github_access_token = models.CharField(null=True, blank=True, max_length=45)
    github_organization = models.ForeignKey(GithubOrganization)


class Repository(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    organization = models.ForeignKey(GithubOrganization, null=True, blank=True)

    @property
    def local_path(self):
        return os.path.join(settings.CLONE_DIRECTORY, str(self.pk))

    def generate_report(self, commit):
        try:
            report = Report.objects.get(commit=commit)
        except Report.DoesNotExist:
            pass
        else:
            return report

        repo = self.checkout(commit=commit)

        errors = reporters.run(self.local_path)
        report = Report.objects.create(
            repository=self,
            commit=commit,
            branch=repo.active_branch.name
        )
        for error_data in errors:
            Issue.objects.create(
                report=report,
                **error_data
            )

        return report

    def checkout(self, commit='master'):
        # If commit is none, we'll get the latest
        try:
            repo = Repo(self.local_path)
        except NoSuchPathError:
            # I guess it was never cloned...
            repo = Repo.init(self.local_path)
            repo.create_remote('origin', url=self.url)

        repo.remotes.origin.fetch()
        bare_master = repo.create_head('master', repo.remotes.origin.refs.master)
        repo.head.set_reference(bare_master)
        repo.head.reset(index=True, working_tree=True)
        return repo

    @property
    def latest_report(self):
        return self.reports.all()[0]


class Report(models.Model):
    repository = models.ForeignKey(Repository, related_name='reports')
    branch = models.CharField(max_length=255)
    commit = models.CharField(max_length=45)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    @property
    def errors(self):
        return self.issues.filter(severity=Issue.ERROR)

    @property
    def warnings(self):
        return self.issues.filter(severity=Issue.WARNING)


class Issue(models.Model):

    ERROR = 0
    WARNING = 1

    SEVERITY_CHOICES = (
        (ERROR, 'Error'),
        (WARNING, 'Warning')
    )

    report = models.ForeignKey(Report, related_name='issues')
    path = models.CharField(max_length=1000)
    line = models.IntegerField()
    column = models.IntegerField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES, default=ERROR)
    message = models.CharField(max_length=1000)
    code = models.CharField(max_length=20, null=True, blank=True)
    reporter = models.CharField(max_length=255)

    def __unicode__(self):
        return '[{}] {} @ {}/{}'.format(
            self.get_severity_display(),
            self.message,
            self.line,
            self.column
        )
