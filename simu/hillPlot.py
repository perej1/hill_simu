
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
    function for plotting Hill estimator convergence in probability.
    n1 = smallest sample size
    n2 = largest sample size
    s = step
    f1 = file path for data
    f2 = file path and name for the plot
    r = number of estimates in one csv
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
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams["font.family"] = 'Times New Roman'
    ax.set_xlim(left=0, right=20000)
    ax.plot(n, q_1, '-r', lw=1, label='1st quartile')
    ax.plot(n, q_2, '-k', lw=1, label='median')
    ax.plot(n, q_3, '-b', lw=1, label='3rd quartile')
    ax.plot(n, val, '--g', alpha=0.75, lw=1, label=r'$ \gamma $')
    ax.set_ylabel(r'$\hat{\gamma}$')
    ax.set_xlabel('n')
    ax.legend()
    ax.set_title('Convergence of the Hill Estimator (%s)' % d.capitalize())
    plt.savefig(f2, format='pdf', dpi=1000)


def main():

    parser = arg.ArgumentParser(
        description="Plots graphs about Hill estimator"
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
