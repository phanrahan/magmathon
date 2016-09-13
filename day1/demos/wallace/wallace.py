#
# Implementatin of wallace trees
#
from magma import *
from mantle import *

def compress2to2():
    return fork([LUT2(I0^I1), LUT2((I0&I1)|(I1&I2))])

def compress3to2():
    return fork([LUT3(I0^I1^I2), LUT3((I0&I1)|(I1&I2)|(I2&I0))])

def column(bits):
    n = len(bits)
    ones = []
    twos = []
    for i in range(0,n,3):
        k = n-i;
        if k >= 2:
            if k >= 3:
                c = compress3to2()
                c(bits[i], bits[i+1], bits[i+2])
            else:
                c = compress2to2()
                c(bits[i], bits[i+1])
            ones.append(c.O[0])
            twos.append(c.O[1])
        else:
            ones.append(bits[3*i])
    return twos, ones

def reduce(bits):
    res = []
    lasttwos = []
    for b in bits:
        twos, ones = column(b)
        res.append(lasttwos + ones)
        lasttwos = twos
    if len(lasttwos) > 0:
        res.append(lasttwos)
    #print map(len, res)
    return res

# returns True if there is 1 bit in each place
def ripple(bits):
    for b in bits:
         if len(b) > 1:
             return False
    return True

def wallace(r):
    while not ripple(r):
        r = reduce(r)
    return r

