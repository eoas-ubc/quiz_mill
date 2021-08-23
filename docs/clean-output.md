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

# Clean output
This script deletes all files in the `output/` folder in the [project file structure](project-file-structure.md).

## How the script works

### Import libraries

+++

```
import click
import os
```

+++

### Delete files function
Recursively travels through the directory, deleting files.

+++

```
def delete_files(path, verbose):
    content = os.listdir(path)

    for f in content:
        file_path = os.path.join(path, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                if verbose:
                    print("Removed", file_path)
            elif os.path.isdir(file_path):
                delete_files(file_path, verbose)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
```

+++

### Main function
Function that will be run when `clean` command is run.

+++

```
@click.command()
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(verbose):
    delete_files("../notebooks/output/", verbose)

if __name__=="__main__":
    main()
```
