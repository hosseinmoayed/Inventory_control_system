import math

def eoq(h , A , D):
    a1 = 2*A*D/h
    eoq = math.sqrt(a1)
    return eoq



def rop(eoq , D , L):
    t = eoq/D
    m = L // t
    rop  = (D*L)-(m*eoq)
    return rop
