---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Workflow

## The base notebook
This is the notebook that all generated notebooks will be based off of. All scripts currently specifically tailored to **two_layers.ipynb**.

![two layers screenshot](two_layers_screenshot.png)

## Steps
### 1. Remove all files from output/ folder
```find notebooks/output/ -type f -exec rm -v {} \;```
### 2. Generate *n* notebooks with random parameters
The below command generates 10 notebooks with random parameters.  
```python quiz_mill/generate_notebooks.py -n <INSERT NUM HERE>```

Read more [here](generate_notebooks.md).
### 3. Filter notebooks into student and solution notebooks
```filter-notebook PATH/TO/UNFILTERED/NOTEBOOKS PATH/TO/FILTERED/NOTEBOOKS/```  
  
Example:  
```filter-notebook notebooks/output/unfiltered/ notebooks/output/filtered/```

Read more [here](filter_notebook.md).
### 4. Send filtered solution notebooks as quizzes to Canvas
```sh quiz_mill/send_to_canvas.sh```
Note: requires Canvas API token to run.

Read more [here](send_to_canvas.md).
