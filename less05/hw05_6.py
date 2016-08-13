# !/usr/bin/env python3
# coding UTF-8
import random
someList = []
for n in range(1,123):
    someList.append(n)
random.shuffle(someList)
for num in someList:
    if num % 3 == 0:
        print(num)
