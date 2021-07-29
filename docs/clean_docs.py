import os

def delete_files(path, verbose):
    content = os.listdir(path)

    for f in content:
        file_path = os.path.join(path, f)
        try:
            if os.path.isfile(file_path):
                if file_path[-2:] == "md" or file_path[-5:] == "ipynb":
                    os.unlink(file_path)
                    if verbose:
                        print("Removed", file_path)
            elif os.path.isdir(file_path):
                delete_files(file_path, verbose)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

if __name__=="__main__":
    delete_files(".", True)
