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

+++

## How the script works

### Import libraries

+++

```
import subprocess
import click
import glob
```

+++

### Main function 
How it works:
1. Gets all "filtered" solution markdown files in **notebooks/output/filtered/solution/**
2. Send each "filtered" solution markdown file to Canvas

+++

```
@click.command()
@click.argument("path", type=str, nargs=1)
@click.option("-i", "--id", default=51824)
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(path, id, verbose):
    md_files = glob.glob(path + "*md")

    if not md_files:
        print('No files to send or directory does not exist.')
        return
    
    for file in md_files:
        process = subprocess.run(["md2canvas", file, "-f", "../token.yaml", "-c", str(id), "-u", "https://canvas.ubc.ca", "-s"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        if verbose:
            print(process.stdout)
```
