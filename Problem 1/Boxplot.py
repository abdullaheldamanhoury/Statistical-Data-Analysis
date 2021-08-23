import numpy as np 
import pandas as pd  
import statistics as st
import matplotlib.pyplot as plt


def box_blot(x):
    
    #load data

    data=sorted(x)


    #2nd quartile (q2)
    
    q2=np.median(data)
    
    
    #1st quartile (q1)

    data1=sorted([i for i in data if i<q2])

    q1=np.median(data1)
    #3rd quartile (q3)

    data3=sorted([j for j in data if j>q2])
    
    q3=np.median(data3)
    #Outliers
    IQR=q3-q1

    olL=np.subtract(q1,(1.5*IQR))
    olr=q3+(IQR*1.5)

    #Extreme outliers
    EolL=q1-(IQR*3)
    Eolr=q3+(IQR*3)

    outliers=[]
    for i in data:
        if i>olr and i<Eolr:
            outliers.append(i)
        
    for j in data:
        if j<olL and j>EolL:
            outliers.append(j)
                

        
    extreme_outliers=[]
    for k in outliers:
        if k>Eolr or k<EolL:
            extreme_outliers.append(k)
            
            
    return q1,q2,q3,IQR,outliers,EolL,Eolr



T=np.loadtxt('Data1.txt')


b=box_blot(T)
        





