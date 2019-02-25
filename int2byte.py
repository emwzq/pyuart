#!/usr/bin/env python3

def int2byte(din):
    data = din
    a = []
    while data != 0:
        y = data % 256;
        data = data // 256;
        a.append(y)
    c = a[::-1]
    b = bytes(c)
    return b

#a = int2byte(0x1a34534569fda7)
#print(a)
#for i in range(0,len(a)):
#    print("%x"%a[i])

