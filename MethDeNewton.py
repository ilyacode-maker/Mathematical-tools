c = 0
def newton(f,x0,fp,eps):
    global c
    if f(x0) < eps:
        return x0

    xn = x0 - f(x0)/fp(x0)
    c+= 1
    return (newton(f,xn,fp,eps), c)

def f(x):
    return x**2 - 2

def fp(x): 
    return 2*x



