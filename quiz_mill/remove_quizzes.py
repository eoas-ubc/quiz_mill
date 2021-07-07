from canvasapi import Canvas
from pathlib import Path
import yaml

path_to_token = Path('token.yaml').resolve()
file = open(path_to_token)
token = yaml.load(file, Loader=yaml.FullLoader)

API_URL = "https://canvas.ubc.ca/"
API_KEY = token

canvas = Canvas(API_URL, token)

course = canvas.get_course(51824)

assignments = course.get_assignments()

quizzes_to_delete = []
for assignment in assignments:
    if 'Two Layers' in str(assignment):
        assignment.delete()