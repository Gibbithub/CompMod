"""code for Checkpoint2 sets gets m and c for line of best fit to data, plus works out error by finding roots and plotting chi-squared near min"""
import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def main():
    dat="testData.txt"
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

    #find all the roots for the error functions
    errmmax=optimize.root(chi2.ChiErrm,np.array([0.4]))
    errmmin=optimize.root(chi2.ChiErrm,np.array([-0.1]))

    errcmax=optimize.root(chi2.ChiErrc,np.array([1.000]))
    errcmin=optimize.root(chi2.ChiErrc,np.array([0.990]))

    #print all the errors in a nice format
    print " Expected value for m is" + str(m)
    print " Positive error in m is" +str(abs(m-errmmax.x)) +"\n Negative error in m is"+str(abs(m-errmmin.x))

    print " Expected value for c is" + str(c)
    print " Positive error in c is" +str(abs(c-errcmax.x)) +"\n Negative error in c is"+str(abs(c-errcmin.x))

    # code used to plot the chi-squared shifted 0 min by 1, used
    plt.plot(deltam,chivalm)
    plt.xlabel("m")
    plt.ylabel("chisquared with min at -1")
    plt.axhline(y=0)
    plt.axvline(x=errmmax.x,color='k',linestyle='dashed')
    plt.axvline(x=errmmin.x,color='k',linestyle='dashed')
    plt.title("How chi-squared varies with delta m ")
    plt.show()

    plt.plot(deltac,chivalc)
    plt.xlabel("c")
    plt.ylabel("chisquared with min at -1")
    plt.axhline(y=0)
    plt.axvline(x=errcmax.x,color='k',linestyle='dashed')
    plt.axvline(x=errcmin.x,color='k',linestyle='dashed')
    plt.title("How chi-squared varies with delta c ")
    plt.show()



main()
