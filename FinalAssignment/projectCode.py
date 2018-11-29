'''Main project code. Uses various classes in other files to run the assigned tasks'''
import numpy as np
import matplotlib.pyplot as plt
from dualExpDec import dualexpdec
from NLL import Nll
import scipy.optimize as optimize

def Part1():
    f=input("input the desired valued for component weighting of p1-component:")
    tau1=input("input the desired valued for tau1:")
    tau2=input("input the desired valued for tau2:")
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

def Part2(data):
    nll=Nll(data,dualexpdec,'t only')

    #minimise Nll for numdec decays
    F=0.5              #0.9
    tau1=1.0               #1.9
    tau2=2.0                   #0.5
    guess_params=np.array([F,tau1,tau2])
    bound=((0.0,1.0),(0.0,10.0),(0.0,10.0))
    results=optimize.minimize(nll.NllEvalexp,guess_params,bounds=bound)
    print't only'
    print results
    for i in range(len(results.x)):
        nll.parameters.append(results.x[i])
    nll.parameters=np.array(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_error1=optimize.root(nll.NllErrexp,minF-0.1).x-minF
    F_error2=optimize.root(nll.NllErrexp,minF+0.1).x-minF
    #F_properr1,F_properr2=properrorfind(nll)
    Fplot=np.linspace(minF+F_error1, minF+F_error2,100)
    Fnll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])

    nll.error_calcindex=1
    tau1_error1=optimize.root(nll.NllErrexp,mintau1-0.1).x-mintau1
    tau1_error2=optimize.root(nll.NllErrexp,mintau1+0.1).x-mintau1
    tau1plot=np.linspace(mintau1+tau1_error1, mintau1+tau1_error2,100)
    tau1nll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.1).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.1).x-mintau2
    tau2plot=np.linspace(mintau2+tau2_error1, mintau2+tau2_error2,100)
    tau2nll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])

    print minF,F_error1,F_error2
    print mintau1,tau1_error1,tau1_error2
    print mintau2,tau2_error1,tau2_error2

    plt.plot(Fplot,Fnll)
    plt.show()
    plt.plot(tau1plot,tau1nll)
    plt.show()
    plt.plot(tau2plot,tau2nll)
    plt.show()





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
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_error1=optimize.root(nll.NllErrexp,minF-0.1).x-minF
    F_error2=optimize.root(nll.NllErrexp,minF+0.1).x-minF
    print minF,F_error1,F_error2
    F_properr1=properrorfind(nll)
    print F_properr1


    nll.error_calcindex=1
    tau1_error1=optimize.root((nll.NllErrexp-0.5),mintau1-0.1).x-mintau1
    tau1_error2=optimize.root((nll.NllErrexp-0.5),mintau1+0.1).x-mintau1
    tau1_properr1=properrorfind(nll)
    print mintau1,tau1_error1,tau1_error2,
    print tau1_properr1

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.1).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.1).x-mintau2
    tau2_properr1=properrorfind(nll)
    print tau2_properr1

    print minF,F_error1,F_error2,F_properr1#,F_properr2
    print mintau1,tau1_error1,tau1_error2,tau1_properr1#,tau1_properr2
    print mintau2,tau2_error1,tau2_error2,tau2_properr1#,tau2_properr2

def properrorfind(nll):
    bound=((0.0,1.0),(0.0,10.0),(0.0,10.0))
    bound=np.array(bound)
    np.delete(bound,nll.error_calcindex)
    print bound
    dnll=-1.0
    pos_error=0
    neg_error=0
    delta= nll.parameters[nll.error_calcindex]*0.1
    print 'delta start',delta
    nll.delta=delta
    counter = 0
    while delta>=0.001:
        while dnll<0.5:
            counter +=1
            params=np.copy(nll.parameters)
            params=np.delete(params,nll.error_calcindex)
            minimised=optimize.minimize(nll.NllErrproper,params)
            dnll=nll.NllErrproper(minimised.x)
            nll.delta+=delta
            print counter
            #print 'dnll',dnll
            #print 'delta pos move', delta
            #print 'nll delta', nll.delta
        #print 'delta min',delta
        delta=delta/2.0
        #print 'delta after mid',delta
        while dnll>0.5:
            params=np.copy(nll.parameters)
            params=np.delete(params,nll.error_calcindex)
            minimised=optimize.minimize(nll.NllErrproper,params)
            dnll=nll.NllErrproper(minimised.x)
            nll.delta-=delta
            #print 'dnll',dnll
            #print 'delta', delta
            #print 'nll.delta', nll.delta
    pos_error=nll.delta
    print 'pos_error',pos_error

    '''dnll=-1.0
    delta=-nll.parameters[nll.error_calcindex]*0.2
    while delta<=-0.001:
        while dnll<0.5:
            params=np.copy(nll.parameters)
            params=np.delete(params,nll.error_calcindex)
            minimised=optimize.minimize(nll.NllErrproper,params)
            dnll=nll.NllErrproper(minimised.x)
            nll.delta+=delta
            print nll.delta
        delta=delta/2.0
        while dnll>0.5:
            params=np.copy(nll.parameters)
            params=np.delete(params,nll.error_calcindex)
            minimised=optimize.minimize(nll.NllErrproper,params)
            dnll=nll.NllErrproper(minimised.x)
            nll.delta-=delta
            print nll.delta
    neg_error=nll.delta'''

    return pos_error # ,neg_error


def main():
    #Part1()
    file=open('datafile-Xdecay.txt','r')
    stringdata=np.array([line.split() for line in file])
    datafull=np.asfarray(stringdata,float)
    n_randints=np.random.randint(len(datafull),size=500)
    data=np.array([datafull[k] k for k in n_randints])
    t_data=np.array([k[0] for k in data])
    theta_data=np.array([k[1] for k in data])
    plt.hist(t_data,bins=85)
    #plt.show()
    plt.hist(theta_data,bins=85)
    #plt.show()
    Part2(t_data)
    Part3(data)


main()
