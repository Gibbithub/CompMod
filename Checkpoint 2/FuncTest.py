"""code for Checkpoint2 sets gets m and c for line of best fit to data, plus works out error by finding roots and plotting chi-squared near min"""
import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def main():
    dat="C:\Users\User\.atom\packages\Numerical Recipes\Checkpoint 2\\testData.txt"
    chi2=lineChi(dat)
    #myMinimiser=Minimiser(chi2.ChiEval,np.array([0.1,1.0]))- my own minimiser doesn't work as well

    #set up arrays of varying m and c and their resulting chi-squared values shifted down to origin then by one to get the error
    m,c= chi2.minimisesci(np.array([0.,0.0]))
    deltam= np.linspace((m-m),(m+m),100)
    deltac= np.linspace((c-0.02*c),(c+0.02*c),100)
    chivalm=np.zeros(100)#
    chivalc=np.zeros(100)
    for i in range (100):
        chivalc[i]=chi2.ChiErrc(deltac[i])
        chivalm[i]=chi2.ChiErrm(deltam[i])
    print m,c
    errmmax=optimize.root(chi2.ChiErrm,np.array([0.4]))
    print errmmax.x
    errmmin=optimize.root(chi2.ChiErrm,np.array([-0.1]))
    print errmmin.x

    errcmax=optimize.root(chi2.ChiErrc,np.array([1.000]))
    print errcmax.x
    errcmin=optimize.root(chi2.ChiErrc,np.array([0.990]))
    print errcmin.x

    # code used to plot the chi-squared shifted 0 min by 1, used
    plt.plot(deltam,chivalm)
    plt.xlabel("m")
    plt.ylabel("chisquared with min at -1")
    plt.axhline(y=0)
    plt.axvline(x=errmmax.x)
    plt.axvline(x=errmmin.x)
    plt.show()

    plt.plot(deltac,chivalc)
    plt.xlabel("c")
    plt.ylabel("chisquared with min at -1")
    plt.axhline(y=0)
    plt.axvline(x=errcmax.x)
    plt.axvline(x=errcmin.x)

    plt.show()



main()
