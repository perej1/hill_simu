#!/bin/bash
#SBATCH --time=0-00:10:00             # 5 mins
#SBATCH --mem-per-cpu=500             # 500MB of memory
#SBATCH --array=100-300:100           # Array from 100 to 200 with 10 jumps
#SBATCH --partition=debug             # Partition
#SBATCH --job-name=simujob            # Name of the job
#SBATCH --output=./output/simujob.%j.out

cd $WRKDIR
ki=$(srun python ksqrt.py -n $SLURM_ARRAY_TASK_ID)
srun python hillSim.py -n $SLURM_ARRAY_TASK_ID -r 10 -k `echo ${ki}` -f ./data -d pareto
