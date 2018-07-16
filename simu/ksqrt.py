'''
Created on June 4, 2018

@author: perej1
'''
import numpy as np
import argparse as arg


def sqrtk(n):
    '''
    Function for k in hill estimator.
    '''
    print(int(np.floor(np.sqrt(n))))

def main():
    parser = arg.ArgumentParser()
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    sqrtk(args.n)

if __name__ == "__main__":
    main()
    
