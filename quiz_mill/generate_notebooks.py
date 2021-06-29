import papermill as pm
import argparse
import random

# Generates specified number of two_layers.ipynb notebooks with random parameters
# Example command to generate 5 notebooks with random parameters:
#   python generate_notebooks.py -n 5

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--number', required=True)

    io_args = parser.parse_args()
    num_of_quizzes = int(io_args.number)

    for i in range(num_of_quizzes):
        sol =       round(random.uniform(0.0, 500.0), 1)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        albedo =    round(random.uniform(0.0, 1.0), 2)

        pm.execute_notebook(
            'notebooks/two_layers.ipynb',
            'notebooks/output/unfiltered/output_two_layers{}.ipynb'.format(i+1), #TODO: replace hard-coded "two_layers" string
            parameters=dict(sol=sol, epsilon1=epsilon1, epsilon2=epsilon1, albedo=albedo)
        )


