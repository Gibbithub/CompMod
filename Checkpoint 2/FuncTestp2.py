import numpy as np
from NLL import Nll
from expDecay import expdec
from Minimines import Minimiser
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def main():
    numdec=input("enter number of decays to be modelled: ")
    #initialise the Nll corresponding to numdec decays
    sample=expdec(0.0000022)
    sample.kilomuon(numdec)
    samplekilo=sample.kilodec.copy()
    nll=Nll(samplekilo)
    #minimise Nll for numdec decays
    min=Minimiser(nll.NllEvalexp,np.array([0.01]))
    tau = min.minimise(0.0000000001)# minimiser minimises to a given accuracy
    nll.tau=tau

    #creates plot data
    deltatau=np.linspace((tau-0.05*tau),(tau+0.05*tau),100)
    nllerrs=np.zeros(100)
    for i in range(100):
        nllerrs[i]=nll.NllErrexp(deltatau[i])

    #calculates the roots and hence the errors
    errminkilo=optimize.root(nll.NllErrexp,tau-0.05*tau)
    errmaxkilo=optimize.root(nll.NllErrexp,tau+0.05*tau)
    errpos= abs(errminkilo.x[0]-tau)
    errneg= abs(errmaxkilo.x[0]-tau)
    print " Expected value for tau is" + str(tau)
    print " The positive error is" + str(errpos) + "\n The negative error is" + str(errneg)

    plt.plot(deltatau,nllerrs)
    plt.xlabel("tau")
    plt.ylabel("nll with min at -0.5")
    plt.axhline(y=0)
    plt.show()


main()
