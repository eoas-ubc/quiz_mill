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

# Environment setup
If you are running on your own machine, you may want to set up a local environment. The below instructions assume you are going to be using conda.

---
## Before you start
Know the basics of Conda (see [here](https://docs.conda.io/en/latest/)).

## Install Conda
- macOS users: [Installing on macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
- Windows users: [Installing on Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- Linux users: [Installing on Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

## Creating the environment from the environment.yml file
1. Open your terminal
2. `cd` to the outermost quiz_mill/ folder
3. Enter the following command in your terminal: ```$ conda create```
4. Activate the environment: ```$ conda activate quiz-mill``` 

## Installing the command-line utilities
To use commands like `filter-notebook` and `generate-notebooks`, we need to install them first.

1. `cd` to the outermost quiz_mill/ folder
2. Enter the following code into the terminal:  
```$ pip install .```
