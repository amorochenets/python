# !/usr/bin/env python3
# coding UTF-8

currentFile1 = open('file1.txt')
currentFile2 = open('file2.txt')
newSet1 = set(currentFile1.read().split())
newSet2 = set(currentFile2.read().split())
print(newSet1 & newSet2, newSet1.difference(newSet2), sep='\n')
currentFile1.close()
currentFile2.close()
