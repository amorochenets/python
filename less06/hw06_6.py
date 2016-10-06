# !/usr/bin/env python3
# coding UTF-8

currentFile = open('file_hw3.txt')
newFile = open('newFile6.txt', 'w')
newList = currentFile.read().split()
summ = 0
for word in newList:
    if word.isdigit():
         summ += int(word)
    elif word[:-1].isdigit():
         summ += int(word[:-1])
newFile.write('Sum of two digit from first file is %s' % summ)
currentFile.close()
newFile.close()
