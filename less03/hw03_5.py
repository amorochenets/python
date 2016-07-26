#!/usr/bin/env python3
#coding UTF-8
from sys import argv
a, b, c = int(argv[1]), int(argv[2]), int(argv[3])
if  a + b > c and a + c > b and b + c >a :
    print('Yes')
else:
    print('No')