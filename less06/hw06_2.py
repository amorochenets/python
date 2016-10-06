# !/usr/bin/env python3
# coding UTF-8
currentFile = open('file.txt')
newFile = open('newFile.txt', 'w')
counter = 1
for line in currentFile:
    newFile.write('%s : %s' % (counter, line))
    counter += 1
newFile.close()
currentFile.close()
