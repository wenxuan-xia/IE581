def myLCG(m, a, c, z):
    """
        general LCG generator
        input:  m, a, c, z
        output: z
    """
    return (a*z+c)%m


def find_loop(m, a, c, z):
    x = []
    flag = 1
    counter = 0
    while flag:
        # print z
        z = myLCG(m, a, c, z)
        if z in x:
            x.append(z)
            print x
            return counter
        else:
            counter += 1
            x.append(z)


def main():
    print find_loop(15, 5, 3, 7)
    print find_loop(15, 5, 3, 6)
    print find_loop(16, 5, 3, 7)
    print find_loop(16, 5, 3, 6)


if __name__ == '__main__':
    main()
