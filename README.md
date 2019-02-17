## Bachelor thesis and simulations
This repository was for my bachelor thesis and simulations for the  thesis. My thesis is related to the field of extreme value theory. In the `kandi` folder there are all the files regarding the thesis itself: 

- the LaTeX source code `kandi.tex`. 
- thesis as a pdf file `kandi.pdf`.
- figures `pareto.pdf` and `cauchy.pdf`.

In the `simu` folder there are all the files concerning the simulations. Purpose of the simulations is to generate independent samples and calculate values for Hill estimator. Hill estimator estimates parameter called extreme value index, that describes the tail behaviour of a distribution. Simulated data is used for two figures which show finite sample behaviour of the Hill estimator. Simulations were executed with the Aalto University's Triton computing cluster.

Here are all the files used for simulations:

- `hillSim.py` contains the simulation code. It is run in fashion `python hillSim.py [arguments]`, where `[arguments]` specify different simulation scenarios.

- `gen_args.py` is used for creating command line arguments of form `python hillSim.py [arguments]`.

- `simujob.py` submits the job to the Triton and starts the execution.

Following files are for plotting the figures in my thesis:

- `hillPlot.py` contains code for plotting and is run in fashion `python hillPlot.py [arguments]`.

- `plot.sh` executes `hillPlot.py` with various arguments and produces the figures. Figures appear in the `kandi` folder.


### Running the simulations

Run

```
python gen_args.py
```
This generates text files containing command line arguments in the folder `args`.

After this submit the job by running
```
sbatch simujob.sh
```
Results will appear in the folder `data`.

Huge thanks for my thesis advisor Matias Heikkilä for all the advice both for mathematics and coding. Simulations follow very closely the same format as Matias Heikkilä's code in repository https://github.com/mapehe/evt-ica-simu.

