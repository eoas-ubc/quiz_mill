---
jupytext:
  cell_metadata_filter: -all
  main_language: bash
  notebook_metadata_filter: -all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Workflow

* First install mamba and conda-lock into your base environment

    conda activate base
    conda install mamba conda-lock
   
* Then create a lock file for your platform and use it to make
  a new environment

    conda-lock -f environment.yml -p osx-64   (or linux-64 or win-64)
    mamba create --name test --file conda*lock*
    conda activate test

* Finally, install the command line utilities using an editable install:

    pip install -e .


  
