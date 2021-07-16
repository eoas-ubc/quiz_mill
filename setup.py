#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools_scm import get_version

setup(
    name='quiz_mill',
    version=get_version(),
    packages=find_packages(include=['quiz_mill']),
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    entry_points={
          'console_scripts': [
              'run-papermill = quiz_mill.run_papermill:main',
              'filter-notebook = quiz_mill.filter_notebook:main',
              'generate = quiz_mill.generate_notebooks:main'
          ]
    },
    keywords='eoas ubc ocese',
    long_description="""canvas quiz creation""")
