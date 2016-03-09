import s1
import numpy as np
from scipy.stats import norm, rankdata, expon

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
    myArrayX = []
    myArrayY = []
    for i in range(0, n):
        MVN, seed = s1.MVNgen(2, rhoMatrix, seed)
        MVN = norm.cdf(MVN)
        myArrayX.append(MVN[0])
        myArrayY.append(MVN[1])

    myArrayX = expon.ppf(myArrayX)
    Xindex = rankdata(myArrayX)
    Yindex = rankdata(myArrayY)

    xmean = np.mean(myArrayX)
    ymean = np.mean(myArrayY)

    upper = 0
    for i in range(0, n):
        upper += (myArrayX[i]-xmean)*(myArrayY[i]-ymean)

    lowerleft = 0
    lowerright = 0
    for i in range(0, n):
        lowerleft += (myArrayX[i] - xmean)**2
        lowerright += (myArrayY[i] - ymean)**2
    lowerleft = np.sqrt(lowerleft)
    lowerright = np.sqrt(lowerright)

    rst = upper/(lowerleft * lowerright)
    print rst
