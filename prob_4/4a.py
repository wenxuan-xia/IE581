import numpy as np

i = 0
rst = 0
lmbd = 35
q = 1.0
temp = 1.0*np.exp(-lmbd)
target = 55.0/67.0

while rst<target:
    rst += temp
    i += 1
    temp = temp*lmbd/i
    print temp

print i
