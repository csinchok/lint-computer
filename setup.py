#!/usr/bin/env python

from distutils.core import setup

setup(
    name='LintComputer',
    version='0.1',
    description='A webapp to automatically lint repositories',
    author='Chris Sinchok',
    author_email='chris@sinchok.com',
    url='https://github.com/csinchok/lint-computer/',
    packages=['lint_computer'],
    install_requires=[
        'flake8',
        'gitpython',
        'django>=1.8,<1.9',
        'logan==0.7.1'
    ],
    entry_points={
        'console_scripts': [
            'lint-computer = lint_computer.runner:main',
        ],
    },
)
