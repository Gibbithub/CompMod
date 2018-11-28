"""Class to create an nll  """
import numpy as np
import scipy.optimize as optimize


class Nll(object):
    def __init__(self,data,decayform,evalmethod):# initiates with a list of data
        self.data=data
        self.decayform=decayform
        self.parameters=[] #np.zeros(no_params) # used to hold values for parameters at minimum
        self.nllmin=0
        self.evalmethod=evalmethod
        self.error_calcindex=0
        self.delta=0

    def NllEvalexp(self,params):# calculates for a given value of tau
        nll=0.
        decay=self.decayform(params)
        decay.evalmethod=self.evalmethod
        for i in range(len(self.data)):
            nll+=np.log(decay.evaluate(self.data[i]))
        #print nll
        #print params
        return -nll

    def NllErrexp(self,param):# shifts to min and then by 0.5 for error purposes
        params=np.copy(self.parameters)
        params[self.error_calcindex]=param
        err=self.NllEvalexp(params)-self.NllEvalexp(self.parameters)-0.5
        return err

    def NllErrproper(self,param):
        params=np.zeros(len(param)+1)
        for i in range(self.error_calcindex):
            params[i]=param[i]
        params[self.error_calcindex]=self.parameters[self.error_calcindex] + self.delta
        for i in range(self.error_calcindex+1,len(self.parameters)):
            params[i]=param[i-1]

        err=self.NllEvalexp(params)-self.NllEvalexp(self.parameters)-0.5
        print 'testing nll',self.NllEvalexp(params)
        print 'min nll',self.NllEvalexp(self.parameters)
        print 'minimisation params',params
        print 'min params',self.parameters
        print 'nll below 0',err
        print 'delta',self.delta
        return err
