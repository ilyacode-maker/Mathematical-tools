#--------------------------- Dichotomie ----------------------#
'''
Ce programme utilise la methode de dichotomie pour donner une 
solution approchee de l'equation f(x)=0 (approximation est par eps/2)
avec f strictement croi/decroi et continue
'''

import math

def dicho(f, a, b, eps): 
    ### a et b sont l'intervalle ou on cherche la solution
    ### eps et l'intervalle de tolerance de la solution
    ### f est la fonction qui correspand a l'eq homogene f(x) = 0
                 
    mn = min(a,b)
    mx = max(a,b)

    if mx - mn < eps:
        return ((a+b) / 2)

    if f(a)*f(b) > 0:
        return None

    if f(a) * f( (a+b)/2 ) < 0:
        return dicho(f, a, (a+b)/2, eps)

    if f(b) * f((a+b) / 2) < 0:
        return dicho(f,(a+b)/2, b, eps)

def fs():
    yield lambda x : x**2 - math.exp(x)
    yield lambda x : math.log(x**2 + 4) - x
    yield lambda x : math.atan(x) - math.cos(x)

for f in fs():
    print(dicho(f, -1, 1, 0.001))