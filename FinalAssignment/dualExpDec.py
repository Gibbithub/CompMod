import numpy as np

# class to decay particles with decay time and decay angle with two contributinf components p1 and p2
class dualexpdec(object):
    def __init__(self, parameters):
        self.tau1=parameters[1]
        self.tau2=parameters[2]
        self.f=parameters[0]

    #returns random theta and t within relevant distribution
    def decay(self):
        logic=True
        while logic :
            t=np.random.uniform(0.0, 10.0)
            theta=np.random.uniform(0.0,2.0*np.pi)
            y=np.random.uniform(0.0,1.0)
            if y < self.evaluate(np.array([t,theta])):
                logic = False
        return t,theta

    #returns a numpy array of 10000 decays
    def kilodecay(self,decaycount):
        data=np.zeros((decaycount,2))
        for i in range (decaycount):
            data[i][0],data[i][1]=self.decay()
        return data

    #evaluates the value of pdf for given t and theta, if only one value if given marginalise over theta first
    def evaluate(self,variables):
        if hasattr(variables, '__len__'):
            p1=(self.f/(3.0*np.pi*self.tau1))*(1+(np.cos(variables[1])**2))*np.exp(-variables[0]/self.tau1)
            p2=((1-self.f)/(self.tau2*np.pi))*(np.sin(variables[1])**2)*np.exp(-variables[0]/self.tau2)
        else:
            p1=(self.f/self.tau1)*np.exp(-variables/self.tau1)
            p2=((1-self.f)/self.tau2)*np.exp(-variables/self.tau2)
        pdf=p1+p2
        return pdf
