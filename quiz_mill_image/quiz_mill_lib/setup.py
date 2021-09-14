#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools_scm import get_version

setup(
    name='quiz_mill',
    version=get_version(),
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    entry_points={
          'console_scripts': [
              'run-papermill = quiz_mill.run_papermill:main',
              'filter = quiz_mill.filter_notebook:main',
              'generate = quiz_mill.generate_notebooks:main',
              'remove = quiz_mill.remove_quizzes:main',
              'send = quiz_mill.send_to_canvas:main',
              'clean = quiz_mill.clean_output:main',
          ]
    },
    keywords='eoas ubc ocese',
    long_description="""canvas quiz creation""")