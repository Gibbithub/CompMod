import numpy as np

# class to decay particles with decay time and decay angle with two contributinf components p1 and p2
class dualexpdec(object):
    def __init__(self, frac,tau1,tau2):
        self.tau1=tau1
        self.tau2=tau2
        self.f=frac

    #returns random theta and t within relevant distribution
    def decay(self):
        logic=True
        while logic :
            t=np.random.uniform(0.0, 10.0)
            theta=np.random.uniform(0.0,2.0*np.pi)
            y=np.random.uniform(0.0,1.0)
            if y < self.evaluate(t,theta):
                logic = False
        return t,theta

    #returns a numpy array of 10000 decays
    def kilodecay(self):
        data=np.zeros((10000,2))
        for i in range (10000):
            data[i][0],data[i][1]=self.decay()
        return data

    #evaluates the value of pdf for given f, t and theta
    def evaluate(self,t,theta):
        p1=(self.f/3.0*np.pi*self.tau1)*(1+(np.cos(theta)**2))*np.exp(-t/self.tau1)
        p2=((1-self.f)/self.tau2*np.pi)*np.sin(theta)**2*np.exp(-t/self.tau2)
        pdf=p1+p2
        return pdf
