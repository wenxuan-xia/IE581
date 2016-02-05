import s1
import matplotlib.pyplot as plt
import numpy

def plot():
    N = 1000
    points = []
    xx = []
    yy = []
    z0 =1234
    for i in range(0, N):
        z0 = s1.midSquare(z0)
        x = z0/10000.0
        xx.append(x)
        z0 = s1.midSquare(z0)
        y = z0/10000.0
        yy.append(y)
    area = []

    for i in range(0, N):
        if [xx[i], yy[i]] in points:
            idx = points.index([xx[i], yy[i]])
            area[idx] += 5
        else:
            points.append([xx[i], yy[i]])
            area.append(5)

    colors = numpy.random.rand(N)
    plt.scatter(xx, yy, area, c=colors, alpha = 0.5)
    plt.show()

def check_loop():
    u = []
    z0 =1234
    flag = 1
    counter = 0
    while flag == 1:
        z0 = s1.midSquare(z0)
        if z0 in u:
            flag = 0
        u.append(z0)
        counter += 1
    print "loop cycle: ", counter


def main():
    u = []
    n = 10
    z0 = 1234

    for i in range(0, n):
        z0 = s1.midSquare(z0)
        u.append(z0/10000.0)
    print "first ten:" , u


if __name__ == "__main__":
    main()
    check_loop()
    plot()
