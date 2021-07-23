---
jupytext:
  formats: ipynb,md:myst
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

```{code-cell} ipython3
from canvasapi import Canvas
import pdb
import json
from pathlib import Path
import os
```

# Getting the Canvas API token

By: Benjamin Chang

+++

### Step 1

Fetch a canvas access token which will be used as your Canvas API key:

- go to `Settings`
- scroll down and click on `+ New Access Token`
- give your token an appropriate name, don't set an expiry date and hit `Generate Token`
- a pop-up looking like this should come up:

![Screen%20Shot%202021-03-24%20at%208.33.52%20PM.png](attachment:Screen%20Shot%202021-03-24%20at%208.33.52%20PM.png)

- copy all of the text in `Token:` and paste it into the local `token.yml` file and you're done!

```{code-cell} ipython3
file = open('token.yml')
token = yaml.load(file, Loader=yaml.FullLoader)

API_URL = "https://canvas.ubc.ca/"
API_KEY = token

canvas = Canvas(API_URL, token)
```

From now on, requests made to Canvas can be done using this `canvas` object we just created above. The `.get_course` method can fetch you a course instance if you provide it with the course ID. (these are the 5-6 numbers found at the end of the URL of your Canvas course.

```{code-cell} ipython3
ahl = canvas.get_course(51824) # this is for the Andrew & Harlan Sanbox course used for testing Canvas stuff
cs103 = canvas.get_course(48359) # this is for a CPSC 103 class (testing on actual class) that I was a TA for
```

```{code-cell} ipython3
print(ahl.name)
print(cs103.name)
```

Documentation for Canvas API can be found here: https://canvasapi.readthedocs.io/en/stable/index.html

But we will go over some basics of the Canvas data structures. Everything in Canvas extends the original generic Canvas object class which at its core has at least an id attribute. Other fields and methods may vary depending on the subclasses you are dealing with but everything has an id attribute which will come in very useful. Here are some examples.

```{code-cell} ipython3
print(ahl.id) # notice that this is the same ID that we used to fetch the course originally
```

The Canvas API does this weird thing where methods that return a list of items are in a PaginatedList data structure. The `get_modules()` method below gets a list of modules of a Canvas course. But see what happens when I try to look at the list.

```{code-cell} ipython3
cs103_modules = cs103.get_modules() 
print(cs103_modules)
```

The workaound here is to **cast** the paginated list as type list.

```{code-cell} ipython3
modules = list(cs103_modules)
print(modules[0:3]) # I am slicing the list here because it gets very long and ugly to read but we are able
                    # to see a few modules and the attributes that constitute the object class
```

```{code-cell} ipython3
for m in modules:
    print(m.name, m.id)
```

Be careful though, the fields (except for ID) are not consitent among the Canvas object types. Some of them might not even have an attribute called `name`! There is a ton of functionality with Canvas API especially with administrative functionality (which doesn't really apply to us), but in general your workflow should always start from the `Course` object itself: https://canvasapi.readthedocs.io/en/stable/course-ref.html 

With the course as the starting point, you will likely be able to fetch and complete anything you need. Some methods related to courses you might find you will need include: `get_assignments()` or `get_folders()`.

+++

### Uploading/Deleting Files

Uploading files occurs at the Course object level, meaning the method call looks something like this:

`course_object.upload(FILE)`

Note that the file may be the file name itself or a path to the file. Building off of the CPSC 103 course above, say I wanted to upload a file called `grading_rubric` into the course, then the function call would go as the following: 

`cs103.upload('grading_rubric')`

Deleting files on the other hand takes place at the File level.

`file_object.delete()`

Note that because this method occurs at the File object level, you must already have access to the File object itself. There are different ways of doing this, one is to manually go through all the files in the course and select out the desired file into a local variable. Another way would actually be to request the file via its ID, which you can find by using the `.id` attribute shown in above examples.

+++

The above demonstrations extend beyond Files and have applications in all the different Canvas objects that could exist in a Course object. E.g. assignments, quizzes, modules, etc. In all cases each object is deleted at its own level while it is uploaded/added to the course via its own method in the Canvas course object.
