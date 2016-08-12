# !/usr/bin/env python3
# coding UTF-8
from sys import argv
if len(argv) >= 3 and argv[1].isdigit() and argv[2].isdigit():
    a, b = int(argv[1]), int(argv[2])
    if a < b:
        for num in range(a, b + 1):
            print(num)
    else:
        for num in range(a, b - 1, -1):
            print(num)
else:
    print('ERR: Please run it with 2 integer digits as arguments!')
