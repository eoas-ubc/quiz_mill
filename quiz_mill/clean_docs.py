import os

def delete_files(path, verbose):
    content = os.listdir(path)

    for f in content:
        file_path = os.path.join(path, f)

        if ("docs/_build/" in file_path) or (".ipynb_checkpoints" in file_path):
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
    delete_files("../docs", True)
