import os.path
import sys

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

from git import Repo


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
    organization = models.ForeignKey(GithubOrganization)

    def generate_report(self):
        pass

    def checkout(self, commit=None):
        # If commit is none, we'll get the latest
        local_path = os.path.join(settings.CLONE_DIRECTORY, self.pk)
        repo = Repo(local_path)


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
