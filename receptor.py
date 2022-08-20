import math
def binario(num):
    n=num
    bin=0
    e=0
    while n>0:
        c=int(n/2)
        r=n-(2*c)
        #el=(math.pow(10, e))
        el=10**e
        bin=bin+(r*el)
        e=e+1
        n=c
    return bin    
         

