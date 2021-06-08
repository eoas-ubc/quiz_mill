#!/usr/bin/env python

from setuptools import setup


setup(
    name='quiz_mill',
    packages=['quiz_mill'],
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    install_requires=[
        "papermill","click"
    ],
    entry_points={
          'console_scripts': [
              'run-papermill = quiz_mill.run_papermill:main',
              'filter-notebook = quiz_mill.filter_notebook:main'
          ]
    },
    long_description="""description""")
