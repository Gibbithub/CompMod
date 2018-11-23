"""code to run for checkpoint 3 in NumRep"""
from IntegratorODE import Integrator
from Interpolater import Interpolater
from ChargeDistribution import ChargeDistribution
import matplotlib.pyplot as plt

def main():
    #set up charge distribution and integrators
    chrg=ChargeDistribution()
    euler=Integrator(-2.,2.,0.,100)
    RK4=Integrator(-2.,2.,0.,100)
    eulermax=Integrator(-2.,2.,0.,1000)
    RK4max=Integrator(-2.,2.,0.,1000)

    #integrate with appropriate method and function
    euler.Euler(chrg)
    RK4.Rk4(chrg)
    eulermax.Euler(chrg)
    RK4max.Rk4(chrg)

    #plot for part 1
    chrg.show('Charge Distribution')
    euler.graph(plt.scatter,'Euler')
    RK4.graph(plt.scatter,'Rk4')
    eulermax.graph(plt.plot,'Euler-1000')
    RK4max.graph(plt.plot,'Rk4-1000')
    plt.xlabel('x')
    plt.ylabel('E(x)')
    plt.title('Electric Field')
    plt.legend()
    plt.show()

    #set up integrator and interpolator for part 2 and integrate using RK4 Method
    current=Interpolater(RK4.x,-RK4.y)
    voltage=Integrator(-2.,2.,0.,500)
    voltage.Rk4(current)

    #optional way to use Euler method for part 2 as well
    currente=Interpolater(euler.x,-euler.y)
    voltagee=Integrator(-2.,2.,0.,500)
    voltagee.Euler(currente)

    #plot the voltage
    voltage.graph(plt.plot,'Rk4')
    voltagee.graph(plt.plot,'Euler')
    plt.title('Voltage')
    plt.xlabel('x')
    plt.ylabel('V(x)')
    plt.legend()
    plt.show()

main()
