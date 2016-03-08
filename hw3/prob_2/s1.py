import numpy as np
import Beasley_Springer_Moro

def constructMatrix(d=3):
    nparray = np.empty((d,d), dtype=float)
    for i in range(0, d):
        for j in range(0, d):
            nparray[i][j] = 1 if (i == j) else 1.0/20
    return nparray

def MVNgen(d, Lambda, seed):
    C_tilt = np.linalg.cholesky(Lambda)
    z = [0]*d
    x = [0]*d
    for i in range(0, d):
        z[i], seed = Beasley_Springer_Moro.Beasley_Springer_Moro(seed)


    for i in range(0, d):
        x[i] = 0
        for j in range(0, i+1):
            x[i] += C_tilt[i][j]*z[j]

    return x, seed

if __name__ == '__main__':
    Lambda = constructMatrix()
    print MVNgen(3, Lambda)
