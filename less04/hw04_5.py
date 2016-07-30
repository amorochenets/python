#!/usr/bin/env python3
#coding UTF-8
from sys import argv
if len(argv) > 2 :
    n = argv[1]
    k = argv[2]
    if n.isdigit() and k.isdigit() :
        inCart = int(k) % int(n)
        perChild = int(k) // int(n)
        print('In cart: ', inCart, '\nEach child has: ', perChild)
    else :
        print('ERR! Arguments should be numbers!')
else :
    print('ERR! Please start script with two arguments!')
    