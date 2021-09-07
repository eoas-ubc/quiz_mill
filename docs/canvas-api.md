---
jupytext:
  formats: ipynb,md:myst
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

# Getting the Canvas API token
Your Canvas API token is used to send your quizzes to Canvas.

+++

## Step 1: Go to user settings
<!-- <img src="user_settings.png" alt="user settings" style="width: 300px;"/> -->
![user settings](user_settings.png)

## Step 2: Scroll down to `Approved Integrations` section of page
<!-- <img src="approved_integrations.png" alt="approved integrations" style="width: 500px;"/> -->
![approved integrations](approved_integrations.png)

## Step 3: Click on `+ New Access Token`
<!-- <img src="token_button.png" alt="new access token button" style="width: 500px;"/> -->
![new access token button](token_button.png)

## Step 4: Give your token an appropriate name, don't set an expiry date and hit `Generate Token`
<!-- <img src="generate_token.png" alt="generate token" style="width: 300px;"/> -->
![generate token](generate_token.png)  

- a pop-up looking like this should come up:
<!-- <img src="generated_token.png" alt="generated token" style="width: 400px;"/> -->
![generated token](generated_token.png)

## Step 5: copy all of the text in `Token:` and paste it into the local `token.yaml` file and you're done!  
  
Credit: https://github.com/phaustin/eoas-wl/tree/main/canvas-api
