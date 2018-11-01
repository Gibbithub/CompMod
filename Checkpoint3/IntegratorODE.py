import numpy as np
import matplotlib.pyplot as plt
import math
from ChargeDistribution import ChargeDistribution
import copy

class Integrator(object):

    def __init__(self,lowerbound,upperbound,lowerboundval,steps):
        self.y=np.zeros(steps)
        self.y[0]=lowerboundval
        self.x=np.linspace(lowerbound,upperbound,steps)
        self.dx=(upperbound-lowerbound)/steps

    def Rk4(self,function):
        for i in range(len(self.x)):
            d1 = function.evaluate( [self.y[i],self.x[i]] )
            d2 = function.evaluate( [self.y[i]+ self.dx/2*d1, self.x[i]+self.dx/2 ] )
            d3 = function.evaluate( [self.y[i]+ self.dx/2*d2, self.x[i]+self.dx/2 ] )
            d4 = function.evaluate( [self.y[i]+ self.dx*d3, self.x[i]+self.dx ] )
            dy = self.dx*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
            self.y[i+1]=dy+self.y[i]
        return x,y


    def Euler(self,function):
        for i in range(len(self.x)):
            dy = float(function.evaluate( [self.y[i],self.x[i]] ))*self.dx
            self.y[i+1]=dy+self.y[i]
        return x,y

    def graph(self,xlabel,ylabel,title):
        plt.plot(self.x,self.y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
