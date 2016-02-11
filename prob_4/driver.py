import s4b
import numpy as np
import matplotlib.pyplot as mpl
def main(x, iseed):
    n = 100000
    # iseed = 1234
    # x = 45
    rst = []
    for i in range(0, n):
        iseed, profit = s4b.newsvendorOneDay(iseed, x)
        rst.append(profit)

    rst = np.array(rst)
    mean = np.average(rst)

    sigma_hat = 0
    for i in range(0, n):
        sigma_hat += (rst[i]-mean)**2
    sigma_hat /= n
    sigma_hat = np.sqrt(sigma_hat)
    se = sigma_hat/np.sqrt(n)
    # print mean
    # print sigma_hat
    # print se
    return mean, sigma_hat, se, iseed

if __name__ == '__main__':
    x = 37
    iseed = 98723
    xarray = []
    yarray = []
    while x<=43:
        xarray.append(x)
        # print "x=", x
        mean, sigma_hat, se, iseed = main(x, iseed)
        print x, " & ", mean, " & ", sigma_hat, " & ", se, " \\\\"
        x += 1
        # print "---"

        yarray.append(mean)
    mpl.plot(xarray, yarray, "-*")
    mpl.show()
