"""A minimiser class that minimises a given function and a set of variables guess that are a good starting point. The varibles are minimised individually so a well behaved min is required"""

import numpy as np
import copy


class Minimiser(object):

    #initialiser to take in a function(which is a method) and a list of parameters
    def __init__(self,function,paramg):
        self.params=paramg
        self.function=function

    # method to minimise the function
    def minimise(self,accuracy):
        for i in range(len(self.params)): # loop over each variable one at a time to minimise each in turn
            localparams=self.params.copy()
            incfactor=self.params[i]*0.2 # this works in this case because our values are relatively close to the origin
            localparams[i]=incfactor + self.params[i]
            while incfactor > accuracy:     # loops till required accuracy is reached
                print self.function(self.params)
                print self.function(localparams)
                if (self.function(self.params))==(self.function(localparams)):
                    incfactor=incfactor*0.85
                    localparams[i]=incfactor + self.params[i]

                # two if statements followed by while loops to decrease or increase a variable in order to find min
                if (self.function(self.params))>(self.function(localparams)):
                    while self.function(self.params)>(self.function(localparams)):
                        print self.function(self.params)
                        self.params[i]=localparams[i]
                        localparams[i]=incfactor+self.params[i]
                    print incfactor
                    incfactor=incfactor/2
                if (self.function(self.params))<(self.function(localparams)):
                    localparams[i]=self.params[i]-2*incfactor
                    while self.function(self.params)>(self.function(localparams)):
                        self.params[i]=localparams[i]
                        localparams[i]=self.params[i]-incfactor
                    incfactor=incfactor/2
        return localparams
