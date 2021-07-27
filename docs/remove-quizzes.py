# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Remove Quizzes
# Script to remove all Two Layers quizzes from Canvas.
#
# ## Running the script

# %% language="bash"
# python ../quiz_mill/remove_quizzes.py

# %% [markdown]
# ## How the script works
#
# ### Import libraries

# %%
from canvasapi import Canvas
from pathlib import Path
import yaml

# %% [markdown]
# ### Set variables
# #### Decide whether to print out statements

# %%
verbose = True

# %% [markdown]
# #### Get tokens

# %%
path_to_token = Path('../token.yaml').absolute()
file = open(path_to_token)
token = yaml.load(file, Loader=yaml.FullLoader)

# %% [markdown]
# #### Get Canvas object

# %%
API_URL = "https://canvas.ubc.ca/"
API_KEY = token

canvas = Canvas(API_URL, token)

# %% [markdown]
# #### Get course object and assignments

# %%
COURSE_NUM = 51824
course = canvas.get_course(COURSE_NUM)
assignments = course.get_assignments()

# %% [markdown]
# ### Delete Two Layers quizzes from Canvas

# %%
quizzes_to_delete = []
for assignment in assignments:
    if 'Two Layers' in str(assignment):
        assignment.delete()
        if verbose:
            print(str(assignment), "deleted")
