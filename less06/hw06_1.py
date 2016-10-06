# !/usr/bin/env python3
# coding UTF-8
someList = ['ipsum', 'dolor', 'sit', 'amet', 'onsectetur', 'adipisicing', 'elit', 'sed', 'iusmod', 'tempor', 'ncididunt']
for word in someList:
    newWord = ''
    for symb in word:
        newWord += symb + symb.capitalize()
    print(newWord)
