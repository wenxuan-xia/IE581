import u16807d

def main():
    seed = 1
    for i in range(0, 10000):
        seed, u16807 = u16807d.u16807d(seed)
    print seed, u16807


if __name__ == '__main__':
    main()
