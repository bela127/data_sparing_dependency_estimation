For running all the experiments in this project a working java and R version has to be installed on the machine.

To install this project on your machine clone the repository and execute the poetry (https://python-poetry.org/) command poetry install. 

To build a  virtual environment we execute the poetry shell command.

The experiments are defined as blueprints in the experiments folder.

Real world data can be downloaded from here: https://efss.qloud.my/index.php/s/oHybxZcjKRJo74N 
unzip into project folder.

To add additional experiments add a blueprint and specify the experiment parameters.

Start the execution of the experiments by executing the run_experiments.py.

After the execution run the desired post experiment script from the post_experiment_computaion folder.

The output graphics are placed in the experiment_results or fig folder.
