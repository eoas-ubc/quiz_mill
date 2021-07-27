import click
import os
import glob
import shutil

@click.command()
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(verbose):
    delete_files("../notebooks/output/", verbose)

def delete_files(path, verbose):
    content = os.listdir(path)

    for f in content:
        file_path = os.path.join(path, f)
        # try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            if verbose:
                print("Removed", file_path)
        elif os.path.isdir(file_path):
            delete_files(file_path, verbose)

if __name__=="__main__":
    main()
