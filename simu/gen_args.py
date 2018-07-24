'''
Created on July 20, 2018

@author: perej1

Script for creating input arguments for Triton simulation.
one combination of arguments is saved in a single file.
E.g. hillSim.py -n 500 -r 2000 -k 22 -d pareto -f ./data.
Furthermore the free parameter k=o(n) is defined here.
'''
import numpy as np

n = np.arange(100, 20001, 50)
r = 2000
d = np.array(["pareto", "cauchy"])
i = 0


def k(n):
    return int(np.floor(np.sqrt(n)))


for ni in n:
    for di in d:
        f = open("./args/args_%s" % (i), "w")
        f.write("hillSim.py -n %s -r %s -k %s -d %s -f ./data"
                % (ni, r, k(ni), di))
        f.close()
        i += 1
