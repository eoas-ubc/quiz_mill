import click
import subprocess
from pathlib import Path
import contextlib


@click.group()
def main():
    pass


@main.command()
@click.argument("parameter_file")
def doit(parameter_file):
    arglist=['papermill','--help']
    result = subprocess.run(arglist, capture_output=True)
    if result.stdout:
        print(f"stdout message: {result.stdout.decode('utf-8')}")
    if result.stderr:
        print(f"stderror message: {result.stderr.decode('utf-8')}")


if __name__ == "__main__":
    main()
