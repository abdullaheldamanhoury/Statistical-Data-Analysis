import numpy as np 
import matplotlib.pyplot as plt


def Central_Limit_Theorem(n):
    
    


    

    av=[]
    for i in range(n):
        f=np.random.uniform(1,7,1000)
        av.append(f)


    avg_dice=sum(av)/n
    plt.hist(avg_dice,bins=100)

    mean=np.mean(avg_dice)
    var=np.var(avg_dice)





    
    
    return mean,var

j=Central_Limit_Theorem(10)

