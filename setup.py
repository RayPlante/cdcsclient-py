import os, sys, subprocess, unittest
from setuptools import setup

setup(name='multibag',
      version='0.1',
      description="cdcsclient -- python-based client library for access the web API of a CDCS server",
      url='https://github.com/usnistgov/cdcsclient-py',
      scripts=[ ],
      packages=['cdcsclient'],
      test_suite="tests.suite",
      test_runner="unittest:TextTestRunner"
)
