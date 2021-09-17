"""
Removes ipynb and py files, leaving only markdown files, so we can run "jb build docs/" without warnings.

Note: user does not need to use this script, unless making edits to Jupyter Book. 
"""

import os

def delete_files(path, verbose):
    content = os.listdir(path)

    for f in content:
        file_path = os.path.join(path, f)

        if ("docs/_build/" in file_path) or (".ipynb_checkpoints" in file_path) or ("docs/notebooks/" in file_path):
            continue

        try:
            if os.path.isfile(file_path):
                if file_path[-2:] == "py" or file_path[-5:] == "ipynb":
                    os.unlink(file_path)
                    # print(file_path)
                    if verbose:
                        print("Removed", file_path)
            elif os.path.isdir(file_path):
                delete_files(file_path, verbose)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if __name__=="__main__":
    try:
        delete_files("../docs", True)
        print('SUCCESS: cleaned docs/ folder.')
    except FileNotFoundError as e:
        print('ERROR: Script must be run from inside inner-most quiz_mill/ folder.')
