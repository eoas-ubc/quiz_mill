import papermill as pm
import random
import click
from pathlib import Path

# Generates specified number of two_layers.ipynb notebooks with random parameters
# Example command to generate 5 notebooks with random parameters:
#   python generate_notebooks.py -n 5

@click.command()
@click.argument("path", type=str, nargs=1)
@click.option("-n", "--number")
def main(path, number):
    path = Path(path).resolve()
    if not path.is_dir():
        print("Directory path does not exist.")
        return

    for i in range(int(number)):
        sol =       round(random.uniform(0.0, 500.0), 1)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        epsilon1 =  round(random.uniform(0.0, 1.0), 2)
        albedo =    round(random.uniform(0.0, 1.0), 2)

        pm.execute_notebook(
            path / "two_layers.ipynb",
            path / "output/unfiltered/output_two_layers{}.ipynb".format(i+1),
            parameters=dict(sol=sol, epsilon1=epsilon1, epsilon2=epsilon1, albedo=albedo)
        )

if __name__=="__main__":
    main()


