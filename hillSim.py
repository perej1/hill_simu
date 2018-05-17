'''
Created on May 15, 2018

@author: perej1
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats._continuous_distns import pareto
from scipy.stats import cauchy




# Own definition for k, which is a parameter in Hill estimator
# kf(n) is such a function that k-> inf and k/n -> 0
# k is now quite large because we want to see some bias
# for small k variance is great but bias would be nonexistent.
def kf(n):
    return (np.ceil(np.power(n, 5/6))).astype(int)





# Function for the hill estimator

def hill(k, data):
    
    
    # Data is sorted into descending order.
    sorted_data = np.sort(data)[::-1]
    # k largest elements.
    kdata = sorted_data[:k]
    # Elementwise natural logarithm.
    logdata = np.log(kdata)
    # The smallest element is subtracted from every element of this list.
    sumdata = logdata - logdata[-1]
    # Sum of elements and normalize with 1/k.
    # This is estimate for extreme value index. 
    estimate = sum(sumdata)/k
    # estimate for tail index
    return np.power(estimate,-1)


def main():
    
    
    # b is the shape parameter of the pareto dist f(x,b) = b/(x^(b+1))
    # n is the sample size
    # r is the amount of n size samples

    b = 3
    n = 10000
    r= 5000
    # Let's create some data from pareto distribution    
    X = pareto.rvs(b, size = n)
    
    
    #Creating everithing necessary for the hill plot.
    est = np.array([])
    
    K = np.arange(1,int(n/3))
    
    # Estimates for different values for k.
    for k in K:
        est=np.append(est, hill(k, X))
        
        
    # Line y=b represents the true value for tail index
    B = b*np.ones(K.shape)
    
   
    #Next let's study asymptotic properties of the hill estimator
    # First the asymptotic convergence in probability
    

    
    nest = np.array([])
    nvec = np.arange(10, n+1)
    
    for i in nvec:
        nest = np.append(nest, hill(kf(i), pareto.rvs(b, size=i)))
    
    
    # Asymptotic convergence in distribution to Normal distribution.
    
    rvec = np.arange(1, r+1)
    rest = np.array([])
    
    for j in rvec:
        rest = np.append(rest, hill(kf(n), pareto.rvs(b, size = n)))
        
        
    N = np.sqrt(kf(n)) * (rest - b)
    
    
# Let's try same with Cauchy distribution if we could see some unpleasant properties of the hill estimator.
# Tail index of the Cauchy distribution is 1.
    Y = cauchy.rvs(size = n)
    estf = np.array([])
    
    
    # Now we calculate the estimates for different values for k.
    for k in K:
        estf=np.append(estf, hill(k, Y))
        
        

    
   
    # The asymptotic convergence in probability
    

    
    nestf = np.array([])
    
    for i in nvec:
        nestf = np.append(nestf, hill(kf(i), cauchy.rvs(size=i)))
    
    
    # Asymptotic convergence in distribution to Normal distribution.
    
    restf = np.array([])
    
    for j in rvec:
        restf = np.append(restf, hill(kf(n), cauchy.rvs(size = n)))
        
        
    Nf = np.sqrt(kf(n)) * (restf - 1)
    
    
    # Line y = 1
    B1 = np.ones(K.shape)
    
    
    # Figures
    
    plt.figure(1)
    plt.plot(K, est)
    plt.plot(K, B)
    plt.xlabel('$k$')
    plt.ylabel(r'$ \hat{\alpha} $' )
    plt.title('Hill Plot (Pareto)')
    
    
    plt.figure(2)
    plt.plot(nvec, nest)
    plt.xlabel('$n$')
    plt.ylabel(r'$ \hat{\alpha} $')
    plt.title('Convergence in Probability (Pareto)')
    
    
    plt.figure(3)
    plt.hist(N, 50)
    plt.xlabel(r'$ \sqrt{k} (\hat{\alpha} - \alpha) $')
    plt.ylabel('freq')
    plt.title('Convergence in Distribution (Pareto)')
    
    
    plt.figure(4)
    plt.plot(K, estf)
    plt.plot(K, B1)
    plt.xlabel('$k$')
    plt.ylabel(r'$ \hat{\alpha} $' )
    plt.title('Hill Plot (Cauchy)')
    
    plt.figure(5)
    plt.plot(nvec, nestf)
    plt.xlabel('$n$')
    plt.ylabel(r'$ \hat{\alpha} $')
    plt.title('Convergence in Probability (Cauchy)')
    plt.figure(6)
    
    plt.hist(Nf, 50)
    plt.xlabel(r'$ \sqrt{k} (\hat{\alpha} - \alpha) $')
    plt.ylabel('Freq')
    plt.title('Convergence in Distribution (Cauchy)')
    plt.show()
    
    


main()
