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
# # Workflow

# %% [markdown]
# ## Skip the details
# Specify the number of quizzes you would like the generate and run the cell below. Note: cell takes some time to run.

# %% language="bash"
# NUM=5
# sh do_all.sh $NUM

# %% [markdown]
# ### Expected Output
# Specified number of quizzes should be under Quizzes section in Andrew & Harlan Sandbox.
# ![quizzes on Canvas](canvas_quizzes.png)

# %% [markdown]
# ## The details
#
# ### Setup
#
# #### Obtain a Canvas API token
# See step 1 of [this Canvas API tutorial](canvas_api.ipynb) and place ```token.yaml``` file in outer ```quiz_mill/``` directory.
#
# #### The base notebook
# This is the notebook that all generated notebooks will be based off of. All scripts currently specifically tailored to **two_layers.ipynb**.
#
# ![two layers screenshot](two_layers_screenshot.png)

# %% [markdown]
# ### Steps
# #### 1. Remove all Two Layers quizzes from Canvas

# %% language="bash"
# python ../quiz_mill/remove_quizzes.py

# %% [markdown]
# Read more [here](remove_quizzes.ipynb).   
#
# #### 2. Remove all files from output/ folder

# %% language="bash"
# find ../notebooks/output/ -type f -exec rm -v {} \;

# %% [markdown]
# #### 3. Generate *n* notebooks with random parameters
# The below command generates 10 notebooks with random parameters.  

# %% language="bash"
# NUM=10
# python ../quiz_mill/generate_notebooks.py -n $NUM

# %% [markdown]
# Read more [here](generate_notebooks.ipynb).
#
# #### 4. Filter notebooks into student and solution notebooks

# %% language="bash"
# filter-notebook ../notebooks/output/unfiltered/ ../notebooks/output/filtered/

# %% [markdown]
# Read more [here](filter_notebook.md).
# #### 5. Send filtered solution notebooks as quizzes to Canvas

# %% language="bash"
# sh ../quiz_mill/send_to_canvas.sh

# %% [markdown]
# Note: requires Canvas API token to run.
#
# Read more [here](send_to_canvas.md).
