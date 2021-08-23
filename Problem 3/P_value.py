import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.stats import norm 


#fun 1
def p_value1(x1,x2):
    
    
    x1=np.array(x1)
    x1_mean=np.mean(x1)
    x1_std=np.std(x1) 
    Ho = x1_mean


    plt.hist(np.random.normal(x1_mean,x1_std,size=1000),bins=100,color='green',label='population')
    plt.legend()


    x2=np.array(x2)
    x2_mean=np.mean(x2)
    x2_std=np.std(x2)

    plt.hist(np.random.normal(x2_mean,x2_std,size=1000),bins=100,color='black',label='samples')
    plt.legend()



    Zo=np.divide(np.subtract(x2_mean,x1_mean),np.divide(x1_std,np.sqrt(1000)))

    P_value=2*(1-norm.cdf(Zo))


    #The boundries
    z1=norm.ppf(0.025)
    z2=-norm.ppf(0.025)

    Y1=np.subtract((z1*x1_std)/np.sqrt(1000),x1_mean)
    Y2=np.add((z2*x1_std)/np.sqrt(1000),x1_mean)

    alpha=0.05
    if P_value >= alpha:
        H="fail to reject null Hypothises"
        
    if P_value < alpha:
        H="reject null Hypothises"
        
    return P_value,H,Y1,Y2

f1=pd.read_csv('Data3-1.txt',sep=',',header=None)
f2=pd.read_csv('Data3-2.txt',sep=',',header=None)
f3=pd.read_csv('Data3-3.txt',sep=',',header=None)

i=p_value1(f1,f3)
        

    
    