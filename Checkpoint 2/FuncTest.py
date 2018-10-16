import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function
import matplotlib.pyplot as plt

def main():
    dat="testData.txt"
    chi2=lineChi(dat)
    myMinimiser=Minimiser(chi2.ChiEval,np.array([0.1,1.0]))

    m,c= myMinimiser.minimisesci()
    deltam= np.linspace((m-m),(m+m),100)
    chivalm=np.zeros(100)
    for i in range (100):
        chivalm[i]=chi2.ChiEval(np.array([deltam[i],c]))-chi2.ChiEval(np.array([m,c]))-1
    print m,c

    plt.plot(deltam,chivalm)
    plt.xlabel("m")
    plt.ylabel("chisquared - 1")
    plt.show()



main()
