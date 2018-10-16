import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def main():
    dat="testData.txt"
    chi2=lineChi(dat)
    #myMinimiser=Minimiser(chi2.ChiEval,np.array([0.1,1.0]))

    m,c= chi2.minimisesci(np.array([0.1,1.0]))
    deltam= np.linspace((m-m),(m+m),100)
    chivalm=np.zeros(100)
    for i in range (100):
        chivalm[i]=chi2.ChiErrm(deltam[i])
    print m,c
    errp=optimize.root(chi2.ChiErrm,np.array([0.4]))
    print errp.x
    errm=optimize.root(chi2.ChiErrm,np.array([-0.1]))
    print errm.x

    plt.plot(deltam,chivalm)
    plt.xlabel("m")
    plt.ylabel("chisquared - 1")
    plt.show()



main()
