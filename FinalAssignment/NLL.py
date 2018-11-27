"""Class to create an nll  """
import numpy as np
import scipy.optimize as optimize


class Nll(object):
    def __init__(self,data,decayform):# initiates with a list of data
        self.data=data
        self.decayform=decayform
        self.parameters=[] #np.zeros(no_params) # used to hold values for parameters at minimum
        self.error_calcindex=0

    def NllEvalexp(self,params):# calculates for a given value of tau
        nll=0.
        decay=self.decayform(params)
        for i in range(len(self.data)):
            nll+=np.log(decay.evaluate(self.data[i]))
        return -nll

    def NllErrexp(self,param):# shifts to min and then by 0.5 for error purposes
        params=self.parameters.copy()
        params[self.error_calcindex]=param
        err=self.NllEvalexp(params)-self.NllEvalexp(self.parameters)-0.5
        return err
