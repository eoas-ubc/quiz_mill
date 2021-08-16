"""
Sends all filtered solution markdown files as quizzes to Canvas.
"""

import subprocess
import click
import glob

@click.command()
@click.argument("path", type=str, nargs=1)
@click.option("-c", "--coursenum", default=51824)
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(path, coursenum, verbose):
    md_files = glob.glob(path + "*md")

    if not md_files:
        print('No files to send or directory does not exist.')
        return
    
    for file in md_files:
        process = subprocess.run(["md2canvas", file, "-f", "../token.yaml", "-c", str(coursenum), "-u", "https://canvas.ubc.ca", "-s"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        if verbose:
            print(process.stdout)
            
if __name__=="__main__":
    main()