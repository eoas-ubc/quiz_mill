"""
Removes all Two Layers quizzes from Canvas.
"""

from canvasapi import Canvas
from pathlib import Path
import yaml
import click

@click.command()
@click.argument("tokenpath", type=str, nargs=1) # path to token.yaml file
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(tokenpath, verbose):

    path_to_token = Path(tokenpath).resolve()
    file = open(path_to_token / "token.yaml")
    token = yaml.load(file, Loader=yaml.FullLoader)

    API_URL = "https://canvas.ubc.ca/"
    API_KEY = token

    canvas = Canvas(API_URL, API_KEY)

    course = canvas.get_course(51824)

    assignments = course.get_assignments()

    for assignment in assignments:
        if 'Two Layers' in str(assignment):
            assignment.delete()
            if verbose:
                print(str(assignment), "deleted")

if __name__=="__main__":
    main()