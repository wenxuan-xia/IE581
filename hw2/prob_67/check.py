import numpy as np
import LaplaceGenerator

def up2s(x, s):
    if (x<=s and x>=0): return 1.0
    return 0.0

def calculate_x_bar_n(xarray, s):
    rst = 0
    for x in xarray:
        rst += up2s(x, s)
    rst /= len(xarray)
    return rst


def main():
    lbda, s, n = 2, 3, 100
    iseed = 404
    xarray = []
    for i in range(0, n):
        x, iseed = LaplaceGenerator.LaplaceGenerator(lbda, iseed)
        xarray.append(x)

    p = calculate_x_bar_n(xarray, s)
    print p


if __name__ == '__main__':
    main()
