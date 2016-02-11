import u16807d
import numpy as np

def sgn(x):
    if x>=0: return 1
    return -1


def LaplaceGenerator(lbda, iseed):
    """
        input:
            lbda    :   lambda
            iseed   :   current seed
        output:
            x       :   random variate obey laplace distribution
            iseed   :   new seed
    """
    iseed, u = u16807d.u16807d(iseed)
    x = -1.0/lbda*sgn(u-0.5)* np.log(1-2*np.abs(u-0.5))
    return x, iseed
