import os.path
import sys

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

from git import Repo
from git.exc import NoSuchPathError


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

    def generate_report(self):
        pass

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


class Report(models.Model):
    repository = models.ForeignKey(Repository)
    commit = models.CharField(max_length=45)


class Error(models.Model):

    ERROR = 0
    WARNING = 1

    SEVERITY_CHOICES = (
        (ERROR, 'Error'),
        (WARNING, 'Warning')
    )

    report = models.ForeignKey(Report)
    path = models.CharField(max_length=1000)
    line = models.IntegerField()
    column = models.IntegerField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    message = models.CharField(max_length=1000)
    reporter = models.CharField(max_length=255)
