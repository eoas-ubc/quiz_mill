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
    test

if __name__ == "__main__":
    main()
