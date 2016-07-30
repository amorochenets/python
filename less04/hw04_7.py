#!/usr/bin/env python3
#coding UTF-8
from sys import argv
import random
if len(argv) > 2 :
    n = argv[1]
    k = argv[2]
    if n.isdigit() and k.isdigit() :
        if float(n) % float(k) == 0 or float(k) % float(n) == 0 : 
            print(1)
        else: 
            print(random.randint(2,1000))
    else :
        print('ERR! Arguments should be numbers!')
else :
    print('ERR! Please start script with two arguments!')
    