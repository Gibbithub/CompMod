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
    plt.title("Time distribution for F=%.2f,Tau1=%.2f,Tau2=%.2f" %(f,tau1,tau2))
    plt.xlabel("decay time(s)")
    plt.ylabel("occurence")
    plt.show()
    plt.hist(thetadist,bins=85)
    plt.title("Theta distribution for F=%.2f,Tau1=%.2f,Tau2=%.2f" %(f,tau1,tau2))
    plt.xlabel("decay angle(radians)")
    plt.ylabel("occurence")
    plt.show()
# The distribution for f in between 1 and 0 is a scaled linear combination of distribution for f=1 and f=0 ( in some some sense these are the extreme distributions)

def Part2(data,f,tau1,tau2):
    nll=Nll(data,dualexpdec,'t only')

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
    nll.nllmin=nll.NllEvalexp(nll.parameters)
    print nll.parameters
    minF,mintau1,mintau2=nll.parameters[0],nll.parameters[1],nll.parameters[2]

    nll.error_calcindex=0
    F_error1=optimize.root(nll.NllErrexp,minF-0.001).x-minF
    F_error2=optimize.root(nll.NllErrexp,minF+0.001).x-minF
    print 'F',minF,F_error1,F_error2
    Fplot=np.linspace(minF+2*F_error1, minF+2*F_error2,300)
    Fnll=np.array([(nll.NllErrexp(k)+0.5) for k in Fplot])
    F_properr=properrorfind(nll)


    nll.error_calcindex=1
    tau1_error1=optimize.root(nll.NllErrexp,mintau1-0.01).x-mintau1
    tau1_error2=optimize.root(nll.NllErrexp,mintau1+0.01).x-mintau1
    print 'tau1', mintau1,tau1_error1,tau1_error2
    tau1plot=np.linspace(mintau1+2*tau1_error1, mintau1+2*tau1_error2,300)
    tau1nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau1plot])
    tau1_properr=properrorfind(nll)

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.001).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.001).x-mintau2
    print 'tau2',mintau2,tau2_error1,tau2_error2
    tau2plot=np.linspace(mintau2+2*tau2_error1, mintau2+2*tau2_error2,300)
    tau2nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau2plot])
    tau2_properr=properrorfind(nll)

    print 'min F,simple errors,proper errors',minF,F_error1,F_error2,F_properr
    print 'min tau1,simple errors,proper errors',mintau1,tau1_error1,tau1_error1,tau1_properr
    print 'min tau2,simple errors,proper errors',mintau2,tau2_error1,tau2_error2,tau2_properr

    return minF,mintau1,mintau2








# Function to minise the NLL for part 3 and return the values at the minimum along with the simple errors and positive proper error
def Part3(data,f,tau1,tau2):

    nll=Nll(data,dualexpdec,'all')
    F=f
    tau1=tau1
    tau2=tau2
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
    F_properr=properrorfind(nll)



    nll.error_calcindex=1
    tau1_error1=optimize.root((nll.NllErrexp),mintau1-0.01).x-mintau1
    tau1_error2=optimize.root((nll.NllErrexp),mintau1+0.01).x-mintau1
    print 'tau1', mintau1,tau1_error1,tau1_error2
    tau1plot=np.linspace(mintau1+2*tau1_error1, mintau1+2*tau1_error2,300)
    tau1nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau1plot])
    tau1_properr=properrorfind(nll)

    nll.error_calcindex=2
    tau2_error1=optimize.root(nll.NllErrexp,mintau2-0.1).x-mintau2
    tau2_error2=optimize.root(nll.NllErrexp,mintau2+0.1).x-mintau2
    print 'tau2',mintau2,tau2_error1,tau2_error2
    tau2plot=np.linspace(mintau2+2*tau2_error1, mintau2+2*tau2_error2,300)
    tau2nll=np.array([(nll.NllErrexp(k)+0.5) for k in tau2plot])
    tau2_properr=properrorfind(nll)

    print 'min F,simple errors,proper error',minF,F_error1,F_error2,F_properr
    print 'min tau1,simple errors,proper error',mintau1,tau1_error1,tau1_error2,tau1_properr
    print 'min tau2,simple errors,proper error',mintau2,tau2_error1,tau2_error2,tau2_properr

    return minF,mintau1,mintau2


#proper error finding function, takes in the nll initialised with nllmin and an error_calcindex which indicates for which parameter the error is to be found
def properrorfind(nll):
    bound=(0.0,1.0),(0.01,9.99),(0.01,9.99)
    bounds=np.array(bound)
    errorparamin=nll.parameters[nll.error_calcindex] #minimum value of the error parameter
    dnll=-1.0 # shift in nll
    pos_error=0
    delta= nll.parameters[nll.error_calcindex]*0.05 # nudge to error parameter
    nll.delta=delta # shift of error parameter from
    counter = 0
    while delta>=0.0001:
        while dnll<0.5:
            errorparam_fix=errorparamin+nll.delta
            bounds[nll.error_calcindex]=(errorparam_fix,errorparam_fix)
            counter +=1
            #print counter,'increasing'
            params=np.copy(nll.parameters)
            params[nll.error_calcindex]=errorparam_fix
            minimised=optimize.minimize(nll.NllErrproper1,params,bounds=bounds)# re- minimisation for bounds of error parameter set to a constant value
            dnll=minimised.fun
            nll.delta+=delta
        delta=delta/2.0
        while dnll>0.5:
            errorparam_fix=errorparamin+nll.delta
            bounds[nll.error_calcindex]=(errorparam_fix,errorparam_fix)
            counter +=1
            #print counter,'decreasing'
            params=np.copy(nll.parameters)
            params[nll.error_calcindex]=errorparam_fix
            minimised=optimize.minimize(nll.NllErrproper1,params,bounds=bounds)
            dnll=minimised.fun
            nll.delta-=delta
    pos_error=nll.delta

    return pos_error

# runs part 1,2 and 3 and plots allows for plotting the distribution for the entire data set
def main():
    Part1(0.5,1.0,2.0)
    Part1(1.0,1.0,2.0)
    Part1(0.0,1.0,2.0)
    file=open('datafile-Xdecay.txt','r')
    stringdata=np.array([line.split() for line in file])
    data=np.asfarray(stringdata,float)
    #n_randints=np.random.randint(len(datafull),size=5000)
    #data=np.array([datafull[k] for k in n_randints])
    t_data=np.array([k[0] for k in data])
    theta_data=np.array([k[1] for k in data])
    '''plt.hist(t_data,bins=85)
    plt.title('t distribution of data')
    plt.xlabel('decay time')
    plt.ylabel('occurence')
    plt.show()
    plt.hist(theta_data,bins=85)
    plt.title('theta distribution of data')
    plt.xlabel('theta')
    plt.ylabel('occurence')
    plt.show()'''
    ft,tau1t,tau2t=Part2(t_data,0.5,1.0,2.0)
    f,tau1,tau2=Part3(data,0.9,1.9,1.5)
    Part1(ft,tau1t,tau2t)
    Part1(f,tau1,tau2)


main()
