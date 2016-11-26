# !/usr/bin/env python3
# coding UTF-8


def write_to_file(filename, *data, count=1):
    f = open(filename, 'w')
    for i in range(count):
        f.write(str(data))
    f.close()

write_to_file('te1.txt', 4, 1, 12,321,3213,3)