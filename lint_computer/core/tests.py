import os
import shutil

from django.test import TestCase

from .models import Repository

from .reporters.pep8 import run_pep8


class RepoTest(TestCase):

    def test_create(self):
        repo = Repository.objects.create(
            name='lint-computer',
            url='git@github.com:csinchok/lint-computer.git'
        )
        assert not os.path.exists(repo.local_path)

        repo.checkout('847c4d39017ebd9c2e4c7468e4628d1bf607bf7f')
        assert os.path.exists(repo.local_path)

        repo.checkout('9d69f1fd59828c1a1380bb415a00dede38464c07')

        # Kill the repo...
        shutil.rmtree(repo.local_path)


class ReportTests(TestCase):

    def setUp(self):
        self.repo = Repository.objects.create(
            name='lint-computer',
            url='git@github.com:csinchok/lint-computer.git'
        )

    def tearDown(self):
        shutil.rmtree(self.repo.local_path)

    def test_report(self):
        report = self.repo.generate_report('9d69f1fd59828c1a1380bb415a00dede38464c07')
        assert len(report.errors) == 16

    def test_pep8(self):
        self.repo.checkout('9d69f1fd59828c1a1380bb415a00dede38464c07')

        errors = run_pep8(self.repo.local_path)
        assert len(errors) == 16
