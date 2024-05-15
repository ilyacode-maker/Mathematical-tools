def fact(n):
    if n == 1 or n == 2:
        return 1

    return fact(n-1) * n
def un(n):
    if n == 0:
        return 1

    return un(n-1) + 1/fact(n)

def limite(ep):
    c = 1
    while True:
        if un(c+1) - un(c) < ep:
            return un(c+1)
        c += 1
