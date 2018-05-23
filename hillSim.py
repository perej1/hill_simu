
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
Own definition for k, which is a parameter in Hill estimator
kf(n) is such a function that k-> inf and k/n -> 0
k is now quite large because we want to see some bias
for small k variance is great but bias would be nonexistent.
'''


def kf(n):
    return (np.ceil(np.power(n, 1/2))).astype(int)


# Function for the hill estimator.


def hill(sample, k):
    sample = sorted(sorted(np.array(sample), reverse=True)[:k])
    sample = np.log(sample) - np.log(sample[0])
    return np.mean(sample[1:])


'''
r amount of n sized samples are created
from pareto and cauchy distributions.
'''


def sim(n, r):
    hill_pareto = np.array([])
    hill_cauchy = np.array([])

    for i in np.arange(0, r):
        X1 = pareto.rvs(3, size=n)
        X2 = cauchy.rvs(1, size=n)
        hill_pareto = np.append(hill_pareto, hill(X1, kf(n)))
        hill_cauchy = np.append(hill_cauchy, hill(X2, kf(n)))

    estimates = pd.DataFrame(
            np.array([hill_pareto, hill_cauchy]).T,
            columns=np.array(["pareto", "cauchy"])
                             )
    estimates.to_csv("hill_estimates.csv", sep=",", encoding="utf-8")


def main():

    parser = arg.ArgumentParser(
            description="Simulates values for hill estimates."
                                )
    parser.add_argument("-n", help="sample size", type=int)
    parser.add_argument("-r", help="number of samples", type=int)
    args = parser.parse_args()
    sim(args.n, args.r)


main()
