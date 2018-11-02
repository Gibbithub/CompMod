"""contains class for interpolating a discrete function into a continuous one"""
import numpy as np
import math
import copy

class Interpolater(object):
    #initiator takes in x and y value for the function
    def __init__(self,x,y):
        self.x=np.copy(x)
        self.y=np.copy(y)

    #evaluates as the midpoint between two x's in the list if x given is not in the list
    def evaluate(self,params):
        x=params[1]
        coord=0
        for i in range(len(self.x)):
            if x==self.x[i]:
                y=self.y[i]
            elif self.x[i]<x:
                coords=i
                y=(self.y[i]+self.y[i+1])/2
        return y
