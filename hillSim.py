
'''
Created on May 15, 2018

@author: perej1
'''
import numpy as np
from scipy.stats import pareto
from scipy.stats import cauchy
import pandas as pd
import argparse as arg


'''
Function for the hill estimator. k(n) is such a function
that k -> inf and k/n -> 0
'''


def hill(sample, k):
    sample = sorted(sorted(np.array(sample), reverse=True)[:k])
    sample = np.log(sample) - np.log(sample[0])
    return np.mean(sample[1:])


'''
function for creating values for hill estimator.
n = sample size
r = number of estimates
k = parameter for hill estimator
f = file path for estimates
d = specifies the distribution
'''


def sim(n, r, k, f, d):
    hill_est = np.array([])

    if d == "pareto":
        for i in np.arange(0, r):
            X = pareto.rvs(3, size=n)
            hill_est = np.append(hill_est, hill(X, k))

    if d == "cauchy":
        for i in np.arange(0, r):
            X = cauchy.rvs(1, size=n)
            hill_est = np.append(hill_est, hill(X, k))

    estimates = pd.DataFrame(hill_est, columns=np.array([d]))
    estimates.to_csv(f, sep=",", encoding="utf-8")


def main():

    parser = arg.ArgumentParser(
            description="Simulates values for hill estimates."
                                )
    parser.add_argument("-n", help="sample size", type=int)
    parser.add_argument("-r", help="number of samples", type=int)
    parser.add_argument("-k", help="k for hill estimator", type=int)
    parser.add_argument("-f", help="file path for csv", type=str)
    parser.add_argument("-d", help="distribution", type=str,
                        choices=("pareto", "cauchy")
                        )
    args = parser.parse_args()
    sim(args.n, args.r, args.k, args.f, args.d)


main()
