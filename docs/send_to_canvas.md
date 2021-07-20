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

# Send to Canvas
Bash script to send "filtered" solution markdown files to Canvas.

## Running the script

Preconditions:  
1. Canvas API token is in a file called token.yaml in project home directory.
2. Command is run from the project home directory 

```{code-cell} ipython3
%%bash
sh ../quiz_mill/send_to_canvas.sh
```

## How the script works
1. Gets all "filtered" solution markdown files in **notebooks/output/filtered/solution/**
2. Send each "filtered" solution markdown file to Canvas
```
files=`ls notebooks/output/filtered/solution/*md`
for file in $files
do
    md2canvas $file -f token.yml -c 51824 -u https://canvas.ubc.ca -s
done
```
