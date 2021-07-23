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
# # Quickstart
# Skip all the details and run the below code cell to generate quizzes and push them to Canvas.

# %% [markdown]
# ## Requirements
# 1. Canvas API token is in outermost `quiz-mill/` folder. Learn how to get the Canvas API token [here]

# %% [markdown]
# Run this code cell (assign NUM variable the desired number of quizzes):

# %% language="bash"
# NUM=5
# sh do_all.sh $NUM 

# %% [markdown]
# What did the above cell do?
# 1. Removed all previous "Two Layers" quizzes from Canvas
# 2. Removed all previous notebooks in `output/` folder
# 3. Generate `NUM` notebooks with randomly generated parameters
# 4. Filter notebooks into student and solution versions
# 5. Push the solution version notebooks to Canvas
