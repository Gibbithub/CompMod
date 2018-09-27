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
    avglist=np.zeros(500)
    for i in range(500):
        newfunc=expdec(0.0000022)
        avglist[i]=newfunc.kilomuon()
    pl.hist(avglist,bins=100)
    pl.show()

main()
