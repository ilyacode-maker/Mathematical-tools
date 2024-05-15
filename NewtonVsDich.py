from MethDeNewton import newton
from dichotomie import dicho

import numpy as np
import matplotlib.pyplot as plt

    
def compare(f, x0, fp):
    Xaxis = np.array([i for i in range(1,11)])
    Yaxis = np.array([newton(f,x0,fp,10**(-i))[1] for i in range(1,11)])

    plt.plot(Xaxis,Yaxis, color='red')

    Xaxis = np.array([i for i in range(1,11)])
    Yaxis = np.array([dicho(f,0,x0,10**(-i))[1] for i in range(1,11)])

    plt.plot(Xaxis,Yaxis)

    plt.show()


compare(lambda x : x**2-2, 4, lambda x : x**2 - 2 )

