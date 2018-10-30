import numpy as np

# class to make a muon decay with exponential distribution
class expdec(object):
    def __init__(self, tau):
        self.tau=tau

    #returns random x with exponential distribution(one muon decay)
    def muondec(self):
        logic=True
        while logic :
            x=np.random.uniform(0.0, 8*self.tau)
            y=np.random.uniform(0.0,self.evaluate(0.0))
            if y < self.evaluate(x):
                logic = False
        return x

    #returns a numpy array of 1000 muon decays
    def kilomuon(self,iter):
        data=np.zeros(iter)
        sum=0
        for i in range (iter):
            decay=self.muondec()
            data[i]=decay
            sum+=decay
        self.kilodec=data
        return sum/1000

    #evaluate the exponential for a given value
    def evaluate(self,x):
        expo=(1/self.tau)*np.exp(-x/self.tau)
        return expo
