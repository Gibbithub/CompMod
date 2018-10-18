"""Class to create an nll  """
import numpy as np
import scipy.optimize as optimize

class Nll(object):
    def __init__(self,data):# initiates with a list of data
        self.data=data
        self.tau=0.

    def NllEvalexp(self,tau):# calculates for a given value of tau
        nll=0.
        if tau==0.:
            tau=0.000000000001
        elif tau<0. :
            tau=-tau
        for i in range (len(self.data)):
            nll += np.log(1/tau)-self.data[i]/tau
        return -nll

    def NllErrexp(self,tau):# shifts to min and then by 0.5 for error purposes
        err=self.NllEvalexp(tau)-self.NllEvalexp(self.tau)-0.5
        return err

    def minimisesci(self,tau):# designed to minimise nll given a guess
        result=optimize.minimize(self.NllEvalexp,tau)
        self.tau=result.x
        return result.x
