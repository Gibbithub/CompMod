import matplotlib.pyplot as pl
import numpy as np
import sys
from expDecay import expdec

#runs a set of 1000 decays and plots distribution, also plots the averages of 500 such sets
def main():
    func=expdec(0.0000022)
    avg=func.kilomuon()
    pl.hist(func.kilodec,bins=100)
    pl.show()
    print ("\n Mean after one experiment is :"+str(avg)+"\n")
    avglist=np.zeros(500)
    sum=0
    for i in range(500):
        newfunc=expdec(0.0000022)
        result=newfunc.kilomuon()
        avglist[i]=result
        sum+=result
    pl.hist(avglist,bins=100)
    stdev=np.std(avglist)
    print ("\n Standard deviation of gaussian is : " + str(stdev)+"\n")
    print ("\n Mean after 500 experiments is: "+str(sum/500)+"\n")
    print ("\n Standard error of the distribution is :"+ str(stdev/(np.sqrt(500)))+"\n")
    print ("\n 68% of individual experiments done will yield a mean within one standard deviation\n if 500 experiments were repeated the new mean will be within one standard error 68% of the time")
    pl.show()
main()
