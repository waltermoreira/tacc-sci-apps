#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand

import os
import sys


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--ignore', 'build']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='server',
    version='0.1.0',
    description='A server to collect analytics from scientific apps.',
    long_description=readme,
    author='Walter Moreira',
    author_email='wmoreira@tacc.utexas.edu',
    url='https://github.com/waltermoreira/server',
    packages=[
        'server',
    ],
    scripts=['bin/analytics_server.py'],
    package_dir={'server':
                 'server'},
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-RESTful'
    ],
    license="MIT",
    zip_safe=False,
    keywords='server',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ],
    cmdclass={'test': PyTest},
    tests_require=['pytest'],
    test_suite='tests',
)