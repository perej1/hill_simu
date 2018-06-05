
'''
Created on June 5, 2018

@author: perej1
'''
import numpy as np
import pandas as pd
import argparse as arg
import matplotlib.pyplot as plt


def pplot(n1, n2, s, f1, f2, r, g, d):
    '''
    function for plotting gamma_h -> gamma convergence in probability.
    n1 = smallest n
    n2 = largest n
    s = step
    f1 = file path for data
    f2 = file path and name for the plot
    r = sample size
    g = true value of the extreme value index
    d = distribution
    '''
    q_1 = np.array([])
    q_2 = np.array([])
    q_3 = np.array([])
    n = np.arange(n1, n2+1, s)
    val = g * np.ones(n.shape)

    for i in n:
        k = int(np.floor(np.sqrt(i)))
        data_i = pd.read_csv("%s/%s-%s-%s-%s.csv" % (f1, i, r, k, d))
        q_1 = np.append(q_1, data_i[d].quantile(0.25))
        q_2 = np.append(q_2, data_i[d].median())
        q_3 = np.append(q_3, data_i[d].quantile(0.75))

    fig, ax = plt.subplots()
    plt.plot(n, q_1, label='1st quantile')
    plt.plot(n, q_2, label='median')
    plt.plot(n, q_3, label='3rd quantile')
    plt.plot(n, val, label=r'$ \gamma $')
    ax.set_ylabel(r'$\hat{\gamma}$')
    ax.set_xlabel('n')
    ax.legend()
    ax.set_title('Asymptotic Convergence of the Hill Estimator')
    plt.savefig(f2)


def main():

    parser = arg.ArgumentParser(
        description="Plots stuff"
    )
    parser.add_argument("-n1", help="lower bound", type=int)
    parser.add_argument("-n2", help="upper bound", type=int)
    parser.add_argument("-s", help="step", type=int)
    parser.add_argument("-f1", help="data file path", type=str)
    parser.add_argument("-f2", help="fig file path", type=str)
    parser.add_argument("-r", help="sample size", type=int)
    parser.add_argument("-p", help="plot type", type=str, choices=("pplot"))
    parser.add_argument("-g", help="extreme value index", type=float)
    parser.add_argument("-d", help="distribution", type=str,
                        choices=("pareto", "cauchy")
                        )

    args = parser.parse_args()

    if args.p == "pplot":
        pplot(args.n1, args.n2, args.s,
              args.f1, args.f2, args.r, args.g, args.d)


if __name__ == "__main__":
    main()
