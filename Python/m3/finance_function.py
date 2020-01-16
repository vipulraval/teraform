def fv (pv, rate, n):
    future= float(pv*(1+rate/100)**n)
    return future
print(fv(1000,10,5))
