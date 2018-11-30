"""Class to create an nll  """
import numpy as np
import scipy.optimize as optimize


class Nll(object):
    # initiates nll with a data set, a class which forms the model to which the data is to be fit and any condtions on the evaluation function of said model
    def __init__(self,data,decayform,evalmethod):
        self.data=data
        self.decayform=decayform
        self.parameters=[] #np.zeros(no_params) # used to hold values for parameters at minimum
        self.nllmin=0 # holds minimum value for the nll
        self.evalmethod=evalmethod
        self.error_calcindex=0 # holds the index of the variable for which errors are being calculated
        self.delta=0 #holds the error on the variable being

    #method evaluates nll for given parameters for the model function
    def NllEvalexp(self,params):
        nll=0.
        decay=self.decayform(params)
        decay.evalmethod=self.evalmethod
        nll = -np.sum(np.log(decay.evaluate(self.data)))
        return nll

    #Method evaluates the nll with only one parameters being changed and the others set to the minimalising values. The method returns the difference between this nll and the minimal nll - 0.5.
    def NllErrexp(self,param):#finding roots for this function gives simple errors
        params=np.copy(self.parameters)
        params[self.error_calcindex]=param
        err=self.NllEvalexp(params)-self.nllmin-0.5
        return err

    #method to evaluate the shift in NLL 
    def NllErrproper1(self,param):
        err = self.NllEvalexp(param)-self.nllmin
        return err
