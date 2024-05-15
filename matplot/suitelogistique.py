from matplotlib.axis import XAxis, YAxis
import numpy as np
import matplotlib.pyplot as plt

def Xn(x,n,mu):
    if n == 0:
        return x
    b = Xn(x, n -1, mu)
    return mu*b*(1-b)



def fmu(mu, x):
    return mu*x*(1-x)

def logistique1(mu, x0, n):
    Xaxis = np.array([i for i in range(n+1)])
    Yaxis = np.array([Xn(x0, i, mu) for i in range(n+1)])

    plt.plot(Xaxis,Yaxis, marker='.')
    plt.grid()
    plt.show()

def logistique2(mu,x0,n):
    #dessiner les couples de la suite
    Xaxis_t = [x0]
    for i in range(n):
        b = Xn(x0,i,mu)
        Xaxis_t.append(b)
        Xaxis_t.append(b)
    

    Yaxis_t = Xaxis_t[1:]
    Yaxis_t.append(Xn(x0,n,mu))


    Xaxis = np.array(Xaxis_t)
    Yaxis = np.array(Yaxis_t)

    plt.plot(Xaxis,Yaxis, color = '#E0E0E0')

    #dessiner la fnct f
    j=np.arange(0,1.002,0.002)
    Yaxe = fmu(mu,j)

    plt.plot(j,Yaxe)

    #dessiner x = y
    plt.plot(np.arange(0,1,0.2), np.arange(0,1,0.2))
    
    plt.grid()
    plt.show()



