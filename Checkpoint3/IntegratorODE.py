import numpy as np
import matplotlib.pyplot as plt
import math
from ChargeDistribution import ChargeDistribution
import copy

class Integrator(object):
    def __init__(self):
        self.integral=[]

    def Rk4(self,lowerbound,upperbound,lowerboundval,steps,function):
        y=np.zeros(steps)
        y[0]=lowerboundval
        x=np.linspace(lowerbound,upperbound,steps)
        dx=(upperbound-lowerbound)/steps
        for i in range(steps-1):
            d1 = function.evaluate( [y[i],x[i]] )
            d2 = function.evaluate( [y[i]+ dx/2*d1, x[i]+dx/2 ] )
            d3 = function.evaluate( [y[i]+ dx/2*d2, x[i]+dx/2 ] )
            d4 = function.evaluate( [y[i]+ dx*d3, x[i]+dx ] )
            dy = dx*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
            y[i+1]=dy+y[i]
        return x,y



    def Euler(self,lowerbound,upperbound,lowerboundval,steps,function):
        y=np.zeros(steps)
        y[0]=lowerboundval
        x=np.linspace(lowerbound,upperbound,steps)
        dx=(upperbound-lowerbound)/steps
        for i in range(steps-1):
            dy = float(function.evaluate( [y[i],x[i]] ))*dx
            y[i+1]=dy+y[i]
        return x,y
