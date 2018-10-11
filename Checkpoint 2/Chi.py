import numpy as np

class lineChi(object):

    def __init__(self,file):
        data=open(file,"r")
        self.x=[]
        self.y=[]
        self.err=[]
        for line in data:
            cols=line.split(" ")
            self.x.append(cols[0])
            self.y.append(cols[1])
            self.err.append(cols[2])

    def ChiEval(self,params):
        chi=0.
        for i in range (len(self.x)):
            chi += ((y[i]-(params[0]*self.x[i]+params[1]))/self.err[i])**2
        return chi

    def minimise(self,m,c):
