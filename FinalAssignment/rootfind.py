import numpy as np
import matplotlib as plt
import scipy.optimize as optimize

class errorfind3d(object):

    def __init__(self,function):
        self.function=function

    #takes in an interval which contains only one root and evaluate the root to a given accuracy
    #def bijectfind(self,x1,x2,acc):
    #    iter=int(np.log(abs(x2-x1)/acc)/np.log(2))+1
    #    for i in range (iter):
        #    xcen=(x1+x2)/2
        #    if abs(self.function(x1)+self.function(xcen)) == abs(self.function(x1))+abs(self.function(xcen)):
        #        x1=xcen
        #    elif abs(self.function(xcen)+self.function(x2)) == abs(self.function(xcen))+abs(self.function(x2)):
        #        x2=xcen
        #return xcen

    def minfind(self,nll):
        dnll=-1.0
        delta= nll.parameters[nll.error_calcindex]*0.2
        while delta>=0.0001:
            while dnll<0.0:
                params=np.copy(nll.parameters)
                params=np.delete(params,nll.error_calcindex)
                minimised=optimize.minimize(nll.NllErrproper,params)
                dnll=nll.NllErrproper(minimised.x)
                nll.delta+=delta
            delta=delta/2.0
            while dnll>0.0:
                params=np.copy(nll.parameters)
                params=np.delete(params,nll.error_calcindex)
                minimised=optimize.minimize(nll.NllErrproper,params)
                dnll=nll.NllErrproper(minimised.x)
                nll.delta-=delta
