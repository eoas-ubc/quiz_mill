---
jupytext:
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

# Command reference

## remove
```remove [OPTIONS] TOKENPATH```   
  
OPTIONS:  
**-v, --verbose** := Cause **remove** to be verbose, showing quizzes deleted.

ARGUMENTS:  
**TOKENPATH** := Required argument. Path to location of `token.yaml` file.  

---
## clean
```clean [OPTIONS]```  
  
OPTIONS:  
**-v, --verbose** := Cause **clean** to be verbose, showing files removed.

---
## generate
```generate [OPTIONS] NOTEBOOKPATH```  
  
OPTIONS:
**-n, --number** \<number> := Specify the number of notebooks to create.  

ARGUMENTS:  
**NOTEBOOKPATH** := Required argument. Path to `notebooks/` folder.  
    
---
## filter
```filter [OPTIONS] OUTPUTPATH```  
  
OPTIONS:  
**-v, --verbose** := Cause **filter** to be verbose, showing student and solution notebooks being saved.

ARGUMENTS:  
**OUTPUTPATH** := Required argument. Path to `output/` folder.  

---
## send
```send [OPTIONS] PATH```  
  
OPTIONS:  
**-c, --coursenum** \<coursenum> := Specify Canvas course number.
**-v, --verbose** := Cause **send** to be verbose, showing student and solution notebooks being saved.
