import numpy as np
import matplotlib.pyplot as plt
from dualExpDec import dualexpdec

def main():
    f=input("input the desired valued for component weighting of p1-component:")
    # generate 10000 decays with the weighting for component p1=f
    equicomponent=dualexpdec(f,1.0,2.0)
    dist=equicomponent.kilodecay()
    tdist=[k[0] for k in dist]
    thetadist=([k[1] for k in dist])

    # plot the time distribution followed by the theta distribution for F=0.5
    plt.hist(tdist, bins=85)
    plt.title("Time distribution for F=%.2f" %(f))
    plt.xlabel("decay time(s)")
    plt.ylabel("occurence")
    plt.show()
    plt.hist(thetadist,bins=85)
    plt.title("Theta distribution for F=%.2f" %(f))
    plt.xlabel("decay angle(radians)")
    plt.ylabel("occurence")
    plt.show()

main()
# The distribution for f in between 1 and 0 is a scaled linear combination of distribution for f=1 and f=0 ( in some some sense these are the extreme distributions)
