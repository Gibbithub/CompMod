"""Class for an integrator object which takes in a function in a range and numerically calculates the integral in discrete form"""
import numpy as np
import matplotlib.pyplot as plt
import math
from ChargeDistribution import ChargeDistribution
import copy

class Integrator(object):

    #initiator takes in the interval over which to differentiate and the value of the integral at start of the interval
    def __init__(self,lowerbound,upperbound,lowerboundval,steps):
        self.y=np.zeros(steps)
        self.y[0]=lowerboundval
        self.x=np.linspace(lowerbound,upperbound,steps)
        self.dx=(upperbound-lowerbound)/steps


    #Two method, one for Rk4 integration and one for
    def Rk4(self,function):
        for i in range(len(self.x)-1):
            d1 = function.evaluate( [self.y[i],self.x[i]] )
            d2 = function.evaluate( [self.y[i]+ self.dx/2*d1, self.x[i]+self.dx/2 ] )
            d3 = function.evaluate( [self.y[i]+ self.dx/2*d2, self.x[i]+self.dx/2 ] )
            d4 = function.evaluate( [self.y[i]+ self.dx*d3, self.x[i]+self.dx ] )
            dy = self.dx*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
            self.y[i+1]=dy+self.y[i]


    def Euler(self,function):
        for i in range(len(self.x)-1):
            dy = function.evaluate( [self.y[i],self.x[i]] )*self.dx
            self.y[i+1]=dy+self.y[i]

    # method to make it easier to plot 
    def graph(self,func,labl):
        func(self.x,self.y,label=labl)
