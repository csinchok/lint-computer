from .pep8 import run_pep8


def run(path):

    errors = []

    for reporter in (run_pep8,):
        errors.extend(reporter(path))

    return errors
