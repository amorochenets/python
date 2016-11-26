# !/usr/bin/env python3
# coding UTF-8


def file2list(filename):
    f = open(filename)
    l = []
    for line in f:
        try:
            l.append(int(line))
        except ValueError as s:
            print(s)
    f.close()
    print(l)

file2list('t92.txt')
