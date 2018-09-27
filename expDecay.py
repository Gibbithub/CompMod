import numpy as np

class expdec(object):
    def __init__(self, tau):
        self.tau=tau

    #returns random x with exponential distribution(one muon decay)
    def muondec(self):
        logic=True
        while logic :
            x=np.random.uniform(self.mean-10*self.width, self.mean+10*self.width)
            y=np.random.uniform(0.0,1.0)
            if y < self.evaluate(x):
                logic = False
        return x

    #returns a numpy arrauy of 1000 muon decays
    def kilomuon(self):
        data=np.zeros(1000)
        sum=0
        for i in range (1000):
            decay=self.muondec()
            data[i]=decay
            sum+=decay
        self.kilodec=data
        return sum/1000

    
