import os
import shutil

from django.test import TestCase

from .models import Repository


class RepoTest(TestCase):

    def test_create(self):

        repo = Repository.objects.create(
            name='lint-computer',
            url='git@github.com:csinchok/lint-computer.git'
        )
        repo.checkout('847c4d39017ebd9c2e4c7468e4628d1bf607bf7f')
        assert os.path.exists(repo.local_path)

        # Kill the repo...
        # shutil.rmtree(repo.local_path)
