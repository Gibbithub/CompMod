"""Class to creat and evaluate the chi squared from a data file and a line given by m and c"""
import numpy as np
import scipy.optimize as optimize

class lineChi(object):

    #initiater reads in file and stores values in useful variable form
    def __init__(self,file):
        self.m=0.
        self.c=0.
        data=open(file,"r")
        self.x=[]
        self.y=[]
        self.err=[]
        for line in data:
            cols=line.split()
            self.x.append(float(cols[0]))
            self.y.append(float(cols[1]))
            self.err.append(float(cols[2]))

    #method to return value of chi- squared given a list of parameters
    def ChiEval(self,params):
        chi=0.
        for i in range (len(self.x)):
            chi += ((self.y[i]-(params[0]*self.x[i]+params[1]))/self.err[i])**2
        return chi

    # methods to return chi-squared(as functions of m and c) with min dipped one below x axis for
    def ChiErrm(self,m):
        chivalm=self.ChiEval(np.array([m,self.c]))-self.ChiEval(np.array([self.m,self.c]))-1.
        return chivalm

    def ChiErrc(self,c):
        chivalc=self.ChiEval(np.array([self.m,c]))-self.ChiEval(np.array([self.m,self.c]))-1.
        return chivalc

    #minimiser using scipy easier to implement within class to get lowest m and c vals
    def minimisesci(self,params):
        result=optimize.minimize(self.ChiEval,params)
        self.m,self.c=result.x
        return result.x
