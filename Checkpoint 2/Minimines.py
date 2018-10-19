"""A minimiser class that minimises a given function and a set of variables guess that are a good starting point. The varibles are minimised individually so a well behaved min is required"""

import numpy as np
import copy
import scipy.optimize as optimize

class Minimiser(object):

    #initialiser to take in a function(which is a method) and a list of parameters as guess
    def __init__(self,function,paramg):
        self.params=paramg
        self.function=function

    # method to minimise the function
    def minimise(self,accuracy):
        for i in range(len(self.params)): # loop over each variable one at a time to minimise each in turn
            localparams=self.params.copy()
            incfactor=self.params[i]*0.5 # this works in this case because our values are relatively close to the origin
            localparams[i]=incfactor + self.params[i] # parameters for self.params to chase down to minimum
            while incfactor > accuracy:     # loops till required accuracy is reached

                if (self.function(self.params))==(self.function(localparams)): # if the parameter stagnates, this perturbs it again
                    incfactor=incfactor*0.95
                    localparams[i]=incfactor + self.params[i]

                elif (self.function(self.params))>(self.function(localparams)):# method that changes the parameter in whichever direction reduces the function (self.params chases localparams)
                    if localparams[i] > self.params[i]:
                        while self.function(self.params)>(self.function(localparams)):
                            self.params[i]=localparams[i]
                            localparams[i]=incfactor+self.params[i]
                        incfactor=incfactor/2
                    elif self.params[i] > localparams[i] :
                        while self.function(self.params)>(self.function(localparams)):
                            self.params[i]=localparams[i]
                            localparams[i]=self.params[i]-incfactor
                        incfactor=incfactor/2

                elif (self.function(self.params))<(self.function(localparams)):# makes sure self.params > localparams
                    x=localparams[i]
                    localparams[i]=self.params[i]
                    self.params[i]=x
        return self.params


    #function uses scipy instead- works better
    def minimisesci(self):
        result=optimize.minimize(self.function,self.params)
        return result.x
