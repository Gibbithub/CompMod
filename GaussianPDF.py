import numpy as np

class MyGaussianPdf(object):
    def __init__(self, mean, width):
        self.mean= float(mean)
        self.width=float(width)

    #return a random value of x with gaussian distribution
    def next(self):
        logic=True
        while logic :
            x=np.random.uniform(self.mean-10*self.width, self.mean+10*self.width)
            y=np.random.uniform(0.0,1.0)
            if y < self.evaluate(x):
                logic = False
        return x


    # to evaluate gaussian at x
    def evaluate(self,x):
        gauss=(1/np.sqrt(2*np.pi*(self.width**2)))*np.exp(-(x-self.mean)**2/2*(self.width**2))
        return gauss
