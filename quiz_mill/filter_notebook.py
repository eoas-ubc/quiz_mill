"""
This script generates student and solution notebook quizzes. It
takes as input a directory path containing the "unfiltered" notebooks
(no questions or answers) and a directory path to output student and
solution versions of each "filtered" notebook. Student notebooks only
contain the questions and the solution notebooks contain the 
questions and answers.

To run:

filter-notebook notebooks/output/unfiltered/ notebooks/output/filtered/ 

"""
import os
import jupytext as jp
from jupytext.cli import jupytext
from pathlib import Path
from nbformat.v4.nbbase import new_code_cell, new_markdown_cell
import click
import re
from .solve_layers import do_two_matrix


@click.command()
@click.argument("jupyin", type=str, nargs=1)
@click.argument("jupyout", type=str, nargs=1)
@click.option("-r", "--remove", is_flag=True, help="Remove answer cells")
@click.option("-a", "--add", is_flag=True, help="Add answer cells with answers")
def main(jupyin,jupyout, remove, add):
    in_folder = Path(jupyin).resolve()
    out_folder = Path(jupyout).resolve()

    # Immediately return if directory does not exists
    if not in_folder.is_dir():
        print("Directory containing unfiltered notebooks does not exist.")
        print(f"Resolved directory path: {in_folder}")
        return
    elif not out_folder.is_dir():
        print("Directory to place filtered notebooks does not exist.")
        print(f"Resolved directory path: {out_folder}")
        return

    # Iterate through each unfiltered notebook and filter it
    for _, _, files in os.walk(in_folder, topdown=False):
        
        for in_file in files:
            nb = jp.read(in_folder / in_file)

            # Parameters
            parameter_cell = ""
            sol = 0.0
            epsilon1 = 0.0
            epsilon2 = 0.0
            albedo = 0.0
            
            # Keep notebook cells up to and including parameter cells 
            # (but remove cell containing default parameters)
            original_cells = []
            for _, the_cell in enumerate(nb['cells']):
                
                # Do not include parameter cell
                if (
                    len(the_cell["metadata"]["tags"]) > 0 and 
                    the_cell["metadata"]["tags"][0] == "parameters"
                    ):
                    continue 

                original_cells.append(the_cell)

                # Get injected parameters for use in answer cell
                if (
                    len(the_cell["metadata"]["tags"]) > 0 and 
                    the_cell["metadata"]["tags"][0] == "injected-parameters"
                    ):
                    parameter_cell = the_cell["source"]
                    parameters = list(parameter_cell.split('\n')[1:-1])
                    sol = float(re.sub("^sol = ", "", parameters[0]))
                    epsilon1 = float(re.sub("^epsilon1 = ", "", parameters[1]))
                    epsilon2 = float(re.sub("^epsilon2 = ", "", parameters[2]))
                    albedo = float(re.sub("^albedo = ", "", parameters[3]))
                    break # Stop adding cells when we reach injected parameters cell

            new_cells = []

            # Add question cells for student book
            source = """\
{}

Given the above parameters, find the temperature of layer 1.

Give your answer to three decimal places.\
""".format(parameter_cell)
            question = new_markdown_cell(source=source)
            question["metadata"]["quesnum"]='1'
            question["metadata"]["ctype"]='question'
            question["metadata"]["question_type"] = "numerical_question"
            new_cells.append(question)

            # Save student notebook
            nb['cells'] = original_cells + new_cells
            out_file = out_folder / "student" / f"{in_file[:-6]}_student"
            out_file = out_file.with_suffix('.md')
            jp.write(nb,out_file,fmt='md:myst')
            out_file = out_file.with_suffix('.ipynb')
            jp.write(nb,out_file)

            # Add solutions
            T1 = do_two_matrix(sol, albedo, epsilon1, epsilon2)[1]
            source = "* {:0.2f}, 3: precision_answer".format(T1)
            answer0 = new_markdown_cell(source=source)
            answer0['metadata']['quesnum'] = '1'
            answer0['metadata']['ctype']='answer'
            new_cells.append(answer0)
            source = """Check this with Python:

```{code-cell} ipython3
:ctype: answer
:quesnum: 1

np.testing.assert_almost_equal(ans,6.383,decimals=3)
```"""
            answer1 = new_markdown_cell(source=source)
            answer1['metadata']['quesnum'] = '1'
            answer1['metadata']['ctype']='answer'
            new_cells.append(answer1)
            
            # Save solution notebook
            nb['cells'] = original_cells + new_cells
            out_file = out_folder / "solution" / f"{in_file[:-6]}_solution"
            print(out_file)
            out_file = out_file.with_suffix('.md')
            jp.write(nb,out_file,fmt='md:myst')
            out_file = out_file.with_suffix('.ipynb')
            jp.write(nb,out_file)
        

if __name__ == "__main__":
    main()
