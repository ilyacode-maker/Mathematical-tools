c = 1
def dic(f,a,b,ep):
    global c

    mx = max(a,b)
    mn = min(a,b)
    m = (a*f(b) -b*f(a))/(f(b)-f(a))
    if abs(f(m)) < ep:
        return m
    if f(m)*f(mn) < 0:
        c +=1
        return dic(f,mn,m,ep)
    elif f(m) * f(mx) < 0:
        c+=1
        return dic(f,m,mx,ep)

def f(x): return x**2 - 4

def dic2(f,x0,x1,ep):
    global c

    x2 = (x0*f(x1) -x1*f(x0))/(f(x1)-f(x0))
    print(x2)
    if abs(f(x2)) < ep:
        c += 1
        return x2
    return dic2(f,x1,x2,ep)


import numpy as np
import math as ma 
print([
    dic2(lambda x: np.log(x)**2 -1 ,11,10, 0.000001),
    dic2(lambda x: ma.exp(x**2) - 5, 11, 10 , 0.000001),
])