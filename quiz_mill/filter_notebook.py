from notebooks.two_layers import find_temps
import sys
sys.path.insert(1, '../notebooks')
import two_layers
"""
This script goes through all the cells in a notebook
and sets the ctype metadata to 'question' and adds
a question number.  Then it makes a second pass through 
each cell and adds a new cell with the same question number
and the metadata answer, with the text 'qxx answer here'

To run:

python write_meta.py in_notebook.md out_notebook.md

"""
import jupytext as jp
from jupytext.cli import jupytext
from pathlib import Path
from nbformat.v4.nbbase import new_code_cell, new_markdown_cell
import click


@click.command()
@click.argument("jupyin", type=str, nargs=1)
@click.argument("jupyout", type=str, nargs=1)
@click.option("-r", "--remove", is_flag=True, help="Remove answer cells") # remove currently doesn't do anything
@click.option("-a", "--add", is_flag=True, help="Add answer cells with answers")
def main(jupyin,jupyout, remove, add):
    in_file = Path(jupyin).resolve()
    out_file = Path(jupyout).resolve()
    print(in_file,out_file)
    nb = jp.read(in_file)
    print(f"{(len(nb),type(nb))=}")
    print(f"keys {list(nb.keys())}")
    for item in ['nbformat', 'nbformat_minor', 'metadata']:
        print(f"{item}:{nb[item]=}")
    for count,the_cell in enumerate(nb['cells']):
        the_cell['metadata']['ctype']='question'
        the_cell['metadata']['quesnum']=count

    # add an answer cell after each question cell
    # currently only adds answers for q2 and q3
    if add:
        answers = get_answers()
        i = 0
        new_cells = []
        for a_cell in nb['cells']:
            new_cells.append(a_cell)
            num = a_cell['metadata']['quesnum']
            
            answer = 'here'
            if num in [2, 3]:
                answer = ': ' + str(answers[i])
                i += 1
            source = f"q{num} answer {answer}"
            
            answer = new_markdown_cell(source=source)
            answer['metadata']['quesnum']=a_cell['metadata']['quesnum']
            answer['metadata']['ctype']='answer'
            new_cells.append(answer)
        nb['cells'] = new_cells

    # remove answer cells
    if remove:
        new_cells = []
        for a_cell in nb['cells']:
            if a_cell['metadata']['ctype'] != 'answer':
                new_cells.append(a_cell)
            
        nb['cells'] = new_cells
    #
    # write two versions of the notebook -- md and ipynb
    #
    out_file = out_file.with_suffix('.md')
    jp.write(nb,out_file,fmt='md:myst')
    out_file = out_file.with_suffix('.ipynb')
    jp.write(nb,out_file)


# get answers from two_layers.py
def get_answers():
    # get parameters
    sol = two_layers.sol
    epsilon1 = two_layers.epsilon1
    epsilon2 = two_layers.epsilon2
    albedo = two_layers.albedo

    # get question answers
    q1 = two_layers.do_two(sol, epsilon1, albedo)
    q2 = two_layers.do_two_matrix(sol, epsilon1, epsilon2, albedo)
    
    return [q1, q2]


if __name__ == "__main__":
    main()
