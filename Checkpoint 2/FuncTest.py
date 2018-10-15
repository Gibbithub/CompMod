import numpy as np
from Chi import lineChi
from Minimines import Minimiser
from Function import Function

def main():
    y=Function()
    myMinimiser=Minimiser(y.eeval,np.array([1.0]))

    print myMinimiser.minimise(0.0001)

main()
