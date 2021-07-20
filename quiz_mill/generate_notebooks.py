import papermill as pm
import random
import click

# Generates specified number of two_layers.ipynb notebooks with random parameters
# Example command to generate 5 notebooks with random parameters:
#   python generate_notebooks.py -n 5

@click.command()
@click.option("-n", "--number")
def main(number):
    for i in range(int(number)):
        sol =       round(random.uniform(0.0, 500.0), 1)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        albedo =    round(random.uniform(0.0, 1.0), 2)

        pm.execute_notebook(
            '../notebooks/two_layers.ipynb',
            '../notebooks/output/unfiltered/output_two_layers{}.ipynb'.format(i+1),
            parameters=dict(sol=sol, epsilon1=epsilon1, epsilon2=epsilon1, albedo=albedo)
        )

if __name__=="__main__":
    main()


