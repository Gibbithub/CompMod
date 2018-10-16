import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def main():
    dat="C:\Users\User\.atom\packages\Numerical Recipes\Checkpoint 2\\testData.txt"
    chi2=lineChi(dat)
    #myMinimiser=Minimiser(chi2.ChiEval,np.array([0.1,1.0]))

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

    plt.plot(deltam,chivalm)
    plt.xlabel("m")
    plt.ylabel("chisquared - 1")
    plt.axhline(y=0)
    plt.show()

    plt.plot(deltac,chivalc)
    plt.xlabel("c")
    plt.ylabel("chisquared - 1")
    plt.axhline(y=0)
    plt.show()



main()
