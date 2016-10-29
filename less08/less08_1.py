# !/usr/bin/env python3
# coding UTF-8

currentFile = open('file1.txt')
newString = currentFile.read()
newSet = set(newString.split())
for word in newSet:
    word.strip(',.-!?')
counter = len(newSet)
print(newSet, counter, sep='\n')
currentFile.close()