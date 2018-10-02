from GaussianPDF import MyGaussianPdf
import sys
import matplotlib.pylab as pl
import numpy as np

def main():
    gaussfun=MyGaussianPdf(10,1)
    data=[]
    data=np.zeros(5000)
    for i in range (5000):
        data[i]=gaussfun.next()
    #data=np.random.normal(0,0.3,3000)
    pl.hist(data,bins=100)
    pl.show()


main()
