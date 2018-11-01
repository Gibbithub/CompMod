from IntegratorODE import Integrator
from Interpolater import Interpolater
from ChargeDistribution import ChargeDistribution

def main():
    chrg=ChargeDistribution()
    euler=Integrator(-2.,2.,0.,50)
    RK4=Integrator(-2.,2.,0.,50)
    euler.Euler(chrg)
    RK4.Rk4(chrg)
    euler.graph('x','E(x)','Euler Integration')
    RK4.graph('x','E(x)','Rk Integration')

main()
