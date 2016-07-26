#!/usr/bin/env python3
#coding UTF-8
from sys import argv
if int(argv[1])%400 == 0 :
    print('Yes')
elif int(argv[1])%4 == 0 and int(argv[1])%100:
    print('Yes')
else:
    print('No')