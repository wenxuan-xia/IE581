import numpy as np
import u16807d

def intensityFunction(t):
    return 3+4.0/(t+1)

def NHPP(num):
    rst = []
    LAMBDA = 7
    s = 0
    seed = 1234
    while num>0:
        seed, u1 = u16807d.u16807d(seed)
        lmbd = intensityFunction(s)
        s += -1/LAMBDA*np.log(u1)
        seed, u2 = u16807d.u16807d(seed)
        if u2*LAMBDA<intensityFunction(s):
            rst.append(s)
            num -= 1
    return rst

if __name__ == '__main__':
    print NHPP(10)
