import os.path
import pep8


class LintComputerReport(pep8.BaseReport):

    def __init__(self, *args, **kwargs):
        super(LintComputerReport, self).__init__(*args, **kwargs)

        self._errors = []

    def error(self, line_number, offset, text, check):
        super(LintComputerReport, self).error(line_number, offset, text, check)

        error = dict(
            path=self.filename,
            line=line_number,
            column=offset,
            message=text,
            reporter='pep8'
        )

        error['code'] = text.split(' ', 1)[0]

        if error['code'].startswith('E'):
            error['severity'] = 0  # Error
        if error['code'].startswith('W'):
            error['severity'] = 1  # Warning

        self._errors.append(error)


def run_pep8(path):
    # First off, can we even run?

    python_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.py'):
                python_files.append(os.path.join(root, f))

    if len(f) == 0:
        return  # We don't have any python files

    pep8style = pep8.StyleGuide(quiet=True, reporter=LintComputerReport)
    result = pep8style.check_files(python_files)

    return result._errors
