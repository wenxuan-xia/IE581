import numpy as np
import u16807d

def constructMatrix(d=3):
    nparray = np.empty((d,d), dtype=float)
    for i in range(0, d):
        for j in range(0, d):
            nparray[i][j] = 1 if (i == j) else 1.0/20
    return nparray

def main():
    Lambda = constructMatrix()
    C_tilt = np.linalg.cholesky(Lambda)
    seed = 1234
    



if __name__ == '__main__':
    main()
