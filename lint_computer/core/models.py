from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Report(models.Model):
    repository = models.ForeignKey(Repository)
    