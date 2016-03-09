import u16807d
import numpy as np
from matplotlib import pyplot as plt

def poisgen(seed, lbmd):
    seed, u = u16807d.u16807d(seed)
    k = 0
    cu = 1
    P = 0
    while P<u:
        P += np.e**(-lbmd)*lbmd**k/cu
        k += 1
        cu *= k
    return seed, k-1

def main():
    n = 100000
    seed = 1234
    lbmd = 2
    xarray = []
    for i in range(0, n):
        seed, x = poisgen(seed, lbmd)
        xarray.append(x)

    xcount = np.bincount(xarray)
    binarray = [0]*8
    cuarray = [0]*8


    for i in range(0, len(xcount)):
        if i<8:
            binarray[i] = xcount[i]
        else:
            binarray[7] += xcount[i]

    total = np.sum(binarray) *1.0

    binarray = binarray/total
    cuarray[0] = binarray[0]

    for i in range(1, 8):
        cuarray[i] = cuarray[i-1] + binarray[i]


    plt.plot(range(0, 8), binarray)
    plt.plot(range(0, 8), cuarray)
    plt.show()
    print cuarray

if __name__ == '__main__':
    main()
