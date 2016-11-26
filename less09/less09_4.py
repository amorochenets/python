# !/usr/bin/env python3
# coding UTF-8

def print_world(world, count=1):
    for i in range(count):
        print(world)

print_world('Hello!', 11)

def my_premax(*nums):
    l = list(nums)
    l.sort()
    return l[-1]

