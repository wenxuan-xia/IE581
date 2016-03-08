import s1
import numpy as np
from scipy.stats import norm, rankdata

def rho():
    nparray = np.empty((2,2), dtype=float)
    for i in range(0, 2):
        for j in range(0, 2):
            if i != j:
                nparray[i][j] =  2*np.sin(np.pi*0.95/6)
            else:
                nparray[i][j] = 1


    return nparray


if __name__ == '__main__':
    n = 10000
    seed = 1234
    rhoMatrix = rho()
    print rhoMatrix
    myArrayX = []
    myArrayY = []
    for i in range(0, n):
        MVN, seed = s1.MVNgen(2, rhoMatrix, seed)
        MVN = norm.cdf(MVN)
        myArrayX.append(MVN[0])
        myArrayY.append(MVN[1])

    Xindex = rankdata(myArrayX)
    Yindex = rankdata(myArrayY)

    # print Xindex
    # print Yindex
    d = Xindex - Yindex
    print d
    dsqr = 0.0
    for i in d:
        dsqr += i**2
    rs = 1.0 - 6*dsqr/(n*(n**2-1))
    print rs
