# !/usr/bin/env python3
# coding UTF-8
inputFile = open('file.txt')
newFile = open('file2.txt', 'w')
# i = 1
# for line in inputFile:
#     newFile.write('%s: %s' % (i, line))
#     i += 1
l = set(inputFile.read().split())
for elem in sorted(l):
    newFile.write(elem + '\n')
# newFile.writelines(sorted(l))

inputFile.close()
newFile.close()
