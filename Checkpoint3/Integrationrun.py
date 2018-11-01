from IntegratorODE import Integrator
from Interpolater import Interpolater
from ChargeDistribution import ChargeDistribution

def main():
    chrg=ChargeDistribution()
    euler=integrator(-2.,2.,0.,500)
    RK4=integrator(-2.,2.,0.,500)
    euler.Euler(chrg.evaluate)
    Rk4.Rk4(chrg.evaluate)
    euler.graph('x','E(x)','Euler Integration')
    Rk4.graph('x','E(x)','Rk Integration')

main()
