'''Main project code. Uses various classes in other files to run the assigned tasks'''
import numpy as np
import matplotlib.pyplot as plt
from dualExpDec import dualexpdec
from NLL import Nll
import scipy.optimize as optimize

def Part1(f, tau1,tau2):
    f=f
    tau1=tau1
    tau2=tau2
    # generate 10000 decays with the weighting for component p1=f
    equicomponent=dualexpdec(np.array([f,tau1,tau2]))
    dist=equicomponent.kilodecay(10000)
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
# The distribution for f in between 1 and 0 is a scaled linear combination of distribution for f=1 and f=0 ( in some some sense these are the extreme distributions)

def Part2(data,f,tau1,tau2):
    nll=Nll(data,dualexpdec,'t only')

    #minimise Nll for numdec decays
    F=f              #0.9
    tau1=tau1              #1.9
    tau2=tau2                  #0.5
    guess_params=np.array([F,tau1,tau2])
    bound=((0.0,1.0),(0.001,9.99),(0.001,9.99))
    results=optimize.minimize(nll.NllEvalexp,guess_params,bounds=bound)
    print't only'
    print results
    for i in range(len(results.x)):
        nll.parameters.append(results.x[i])
    nll.parameters=np.array(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_error1=optimize.root(nll.NllErrexp,minF-0.001).x-minF
    F_error2=optimize.root(nll.NllErrexp,minF+0.001).x-minF
    print 'F',minF,F_error1,F_error2
    Fplot=np.linspace(minF+2*F_error1, minF+2*F_error2,300)
    Fnll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])

    nll.error_calcindex=1
    tau1_error1=optimize.root(nll.NllErrexp,mintau1-0.001).x-mintau1
    tau1_error2=optimize.root(nll.NllErrexp,mintau1+0.001).x-mintau1
    print 'tau1', mintau1,tau1_error1,tau1_error2
    tau1plot=np.linspace(mintau1+2*tau1_error1, mintau1+2*tau1_error2,300)
    tau1nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau1plot])

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.001).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.001).x-mintau2
    print 'tau2',mintau2,tau2_error1,tau2_error2
    tau2plot=np.linspace(mintau2+2*tau2_error1, mintau2+2*tau2_error2,300)
    tau2nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau2plot])

    print 'min F,simple errors',minF,F_error1,F_error2
    print 'min tau1,simple errors',mintau1,tau1_error1,tau1_error2
    print 'min tau2,simple errors',mintau2,tau2_error1,tau2_error2

    plt.plot(Fplot,Fnll)
    plt.title('Simple Errors on F ( t dataset only)')
    plt.xlabel('Fraction of P1')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=minF+F_error1,color='k',linestyle='dashed',label= ('x=%.2f'%(minF+F_error1)))
    plt.axvline(x=minF+F_error2,color='k',linestyle='dashed',label= ('x=%.2f'%(minF+F_error2)))
    plt.legend()
    plt.show()

    plt.plot(tau1plot,tau1nll)
    plt.title('Simple Errors on Tau1 (t dataset only)')
    plt.xlabel('Tau1')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=mintau1+tau1_error1,color='k',linestyle='dashed',label= ('x=%.2f'%(mintau1+tau1_error1)))
    plt.axvline(x=mintau1+tau1_error2,color='k',linestyle='dashed',label=('x=%.2f'%(mintau1+tau1_error2)))
    plt.legend()
    plt.show()

    plt.plot(tau2plot,tau2nll)
    plt.title('Simple Errors on Tau2 (t dataset only)')
    plt.xlabel('Tau2')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=mintau2+tau2_error1,color='k',linestyle='dashed',label=('x=%.2f'%(mintau1+tau2_error1)))
    plt.axvline(x=mintau2+tau2_error2,color='k',linestyle='dashed',label=('x=%.2f'%(mintau1+tau2_error2)))
    plt.legend()
    plt.show()

    return minF,mintau1,mintau2









def Part3(data):

    #print data
    nll=Nll(data,dualexpdec,'all')
    #minimise Nll for numdec decays
    F=0.5
    tau1=1.0
    tau2=2.0
    guess_params=np.array([F,tau1,tau2])
    bound=((0.0,1.0),(0.0,10.0),(0.0,10.0))
    results=optimize.minimize(nll.NllEvalexp,guess_params,bounds=bound)
    print 'all'
    print results
    for i in range(len(results.x)):
        nll.parameters.append(results.x[i])
    nll.parameters=np.array(nll.parameters)
    nll.nllmin=nll.NllEvalexp(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_error1=optimize.root(nll.NllErrexp,minF-0.01).x-minF
    F_error2=optimize.root(nll.NllErrexp,minF+0.01).x-minF
    print 'F',minF,F_error1,F_error2,
    Fplot=np.linspace(minF+2*F_error1, minF+2*F_error2,300)
    Fnll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])


    nll.error_calcindex=1
    tau1_error1=optimize.root((nll.NllErrexp),mintau1-0.01).x-mintau1
    tau1_error2=optimize.root((nll.NllErrexp),mintau1+0.01).x-mintau1
    print 'tau1', mintau1,tau1_error1,tau1_error2
    tau1plot=np.linspace(mintau1+2*tau1_error1, mintau1+2*tau1_error2,300)
    tau1nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau1plot])

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.1).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.1).x-mintau2
    print 'tau2',mintau2,tau2_error1,tau2_error2
    tau2plot=np.linspace(mintau2+2*tau2_error1, mintau2+2*tau2_error2,300)
    tau2nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau2plot])

    print 'min F,simple errors,proper error',minF,F_error1,F_error2,F_properr1#,F_properr2
    print 'min tau1,simple errors,proper error',mintau1,tau1_error1,tau1_error2,tau1_properr1#,tau1_properr2
    print 'min tau2,simple errors,proper error',mintau2,tau2_error1,tau2_error2,tau2_properr1#,tau2_properr2

    plt.plot(Fplot,Fnll)
    plt.title('Simple Errors on F (entire dataset)')
    plt.xlabel('Fraction of P1')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=minF+F_error1,color='k',linestyle='dashed',label= ('x=%.3f'%(minF+F_error1)))
    plt.axvline(x=minF+F_error2,color='k',linestyle='dashed',label= ('x=%.3f'%(minF+F_error2)))
    plt.legend()
    plt.show()

    plt.plot(tau1plot,tau1nll)
    plt.title('Simple Errors on Tau1 (entire dataset)')
    plt.xlabel('Tau1')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=mintau1+tau1_error1,color='k',linestyle='dashed',label= ('x=%.3f'%(mintau1+tau1_error1)))
    plt.axvline(x=mintau1+tau1_error2,color='k',linestyle='dashed',label=('x=%.3f'%(mintau1+tau1_error2)))
    plt.legend()
    plt.show()

    plt.plot(tau2plot,tau2nll)
    plt.title('Simple Errors on Tau2 (entire dataset)')
    plt.xlabel('Tau2')
    plt.ylabel('Change in Nll')
    plt.axhline(y=0.5, linestyle='dashed')
    plt.axvline(x=mintau2+tau2_error1,color='k',linestyle='dashed',label=('x=%.3f'%(mintau1+tau2_error1)))
    plt.axvline(x=mintau2+tau2_error2,color='k',linestyle='dashed',label=('x=%.3f'%(mintau1+tau2_error2)))
    plt.legend()
    plt.show()

def properrorfind(nll):
    bound=(0.0,1.0),(0.01,9.99),(0.01,9.99)
    bounds=np.array(bound)
    errorparamin=nll.parameters[nll.error_calcindex]
    dnll=-1.0
    pos_error=0
    neg_error=0
    delta= nll.parameters[nll.error_calcindex]*0.05
    print 'delta start',delta
    nll.delta=delta
    counter = 0
    while delta>=0.001:
        while dnll<0.5:
            errorparam_fix=errorparamin+nll.delta
            bounds[nll.error_calcindex]=(errorparam_fix,errorparam_fix)
            counter +=1
            print counter,'increasing'
            params=np.copy(nll.parameters)
            params[nll.error_calcindex]=errorparam_fix
            minimised=optimize.minimize(nll.NllErrproper1,params,bounds=bounds)
            dnll=minimised.fun
            nll.delta+=delta
        delta=delta/2.0
        while dnll>0.5:
            errorparam_fix=errorparamin+nll.delta
            bounds[nll.error_calcindex]=(errorparam_fix,errorparam_fix)
            counter +=1
            print counter,'decreasing'
            params=np.copy(nll.parameters)
            params[nll.error_calcindex]=errorparam_fix
            minimised=optimize.minimize(nll.NllErrproper1,params,bounds=bounds)
            dnll=minimised.fun
            nll.delta-=delta

    pos_error=nll.delta
    print 'pos_error',pos_error

    return pos_error

# part 4 calculates the proper errors for part 2 and 3
def part4for3():
    nll=Nll(data,dualexpdec,'all')
    #minimise Nll for numdec decays
    F=0.5
    tau1=1.0
    tau2=2.0
    guess_params=np.array([F,tau1,tau2])
    bound=((0.0,1.0),(0.001,9.99),(0.001,9.99))
    results=optimize.minimize(nll.NllEvalexp,guess_params,bounds=bound)
    print 'all'
    print results
    for i in range(len(results.x)):
        nll.parameters.append(results.x[i])
    nll.parameters=np.array(nll.parameters)
    nll.nllmin=nll.NllEvalexp(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_properr1=properrorfind(nll)
    print 'proper F error',F_properr1


    nll.error_calcindex=1
    tau1_properr1=properrorfind(nll)
    print 'proper tau1 error',tau1_properr1

    nll.error_calcindex=2
    tau2_properr1=properrorfind(nll)
    print 'proper tau2 error',tau2_properr1

    print 'min F,proper error',minF,F_properr1
    print 'min tau1,proper error',mintau1,tau1_properr1
    print 'min tau2,proper error',mintau2,tau2_properr


def part4for2(f,tau1,tau2):
    nll=Nll(data,dualexpdec,'t only')

    #minimise Nll for numdec decays
    F=f
    tau1=tau1
    tau2=tau2
    guess_params=np.array([F,tau1,tau2])
    bound=((0.0,1.0),(0.001,9.99),(0.001,9.99))
    results=optimize.minimize(nll.NllEvalexp,guess_params,bounds=bound)
    print't only'
    print results
    for i in range(len(results.x)):
        nll.parameters.append(results.x[i])
    nll.parameters=np.array(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_properr1=properrorfind(nll)
    print 'proper F error (t data only)',F_properr1


    nll.error_calcindex=1
    tau_properr1=properrfind(nll)
    print 'proper tau1 error (t data only)',tau1_properr1

    nll.error_calcindex=2
    tau2_properr1=properrfind(nll)
    print 'proper tau2 error ( t data only)',tau2_properr1

    print 'min F,simple errors',minF,F_properr1
    print 'min tau1,simple errors',mintau1,tau1_properr1
    print 'min tau2,simple errors',mintau2,tau2_properr1


def main():
    #Part1(0.5,1.0,2.0)
    file=open('datafile-Xdecay.txt','r')
    stringdata=np.array([line.split() for line in file])
    data=np.asfarray(stringdata,float)
    #n_randints=np.random.randint(len(datafull),size=5000)
    #data=np.array([datafull[k] for k in n_randints])
    t_data=np.array([k[0] for k in data])
    theta_data=np.array([k[1] for k in data])
    #plt.hist(t_data,bins=85)
    #
    #plt.show()
    #plt.hist(theta_data,bins=85)
    #plt.show()
    #Part3(data)
    Part2(t_data,0.5,1.0,2.0)
    Part3(data)
    #Part2(t_data,0.5,2.0,1.0)
    #Part2(t_data,0.5,1.5,1.5)
    #part2(t_data,0.8,1.5,0.5)


main()
