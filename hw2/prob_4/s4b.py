import u16807d
import numpy as np

def poisgen(lmbd, target):
    """
        input:
            lmbd,
            target  -   uniform(0,1)
        output:
            k       -   possion-k
    """
    i, rst, q = 0.0, 0.0, 1.0
    temp = 1.0*np.exp(-lmbd)

    while rst < target:
        rst += temp
        i += 1
        temp = temp*lmbd/i

    return i-1

def newsvendorOneDay(iseed, x):
    """
        input:
            iseed   :   uniform random seed
            x       :   daily purchased newspaper
        output:
            iseed   :   new value of iseed
            profit  :   profit on this day
    """
    c, s, w = 15, 70, 3
    lmda = 35
    iseed, u = u16807d.u16807d(iseed)
    pois = poisgen(lmda, u)

    profit = 0
    if (x>pois):
        profit = (s-c)*pois - (c-w)*(x-pois)
    else:
        profit = (s-c)*x

    return iseed, profit
