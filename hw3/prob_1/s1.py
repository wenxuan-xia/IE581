import numpy as np
import Beasley_Springer_Moro

def constructMatrix(d=3):
    nparray = np.empty((d,d), dtype=float)
    for i in range(0, d):
        for j in range(0, d):
            nparray[i][j] = 1 if (i == j) else 1.0/20
    return nparray

def main(d=3):
    Lambda = constructMatrix()
    C_tilt = np.linalg.cholesky(Lambda)
    seed = 2345
    z = [0]*d
    x = [0]*d
    for i in range(0, d):
        z[i], seed = Beasley_Springer_Moro.Beasley_Springer_Moro(seed)

    for i in range(0, d):
        for j in range(0, i+1):
            x[i] = C_tilt[i][j]*z[j] + 0

    return x

if __name__ == '__main__':
    print main()
