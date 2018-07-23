#!/bin/bash
#SBATCH --mem-per-cpu=10                # Memory limit set to 10MB
#SBATCH -t 0-00:30:00                   # Time limit set to 30 min
#SBATCH -a 0-797                        # Array from 0 to 797
#SBATCH -J simujob                      # Job name
#SBATCH -o ./output/slurm-%A_%a.out     # Output directory specified

module load anaconda3
srun python $(< ./args/args_$SLURM_ARRAY_TASK_ID)
