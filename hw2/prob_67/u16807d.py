def u16807d(iseed):
    """
        input: iseed
        output: iseed, u16807d
    """

    u16807dd = 0
    while (u16807dd<=0 or u16807dd>=1):
        iseed = (iseed*16807)%2147483647
        u16807dd = iseed/2147483648.0

    return iseed, u16807dd
