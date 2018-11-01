import numpy as np
import math
import copy

class Interpolater(object):
    def __init__(self,x,y):
        self.x=copy(x)
        self.y=copy(y)

    def evaluate(self,params):
        x=params[1]
        coord=0
        for i in range(len(self.x)):
            if x==self.x[i]:
                return self.y[i]
            elif self.x[i]<x:
                coords=i
        y=(self.y[i]+self.y[i+1])/2self.
        return y
