# !/usr/bin/env python3
# coding UTF-8

# for i in 'hello world':
#     print(end='_')
#     if i == 'o':
#         continue
#     print(i*2, end='')

# i = 5
# while i < 15:
#     print(i)
#     i += 2
newList = []
while True:
    word = input('Please enter one word: ')
    if word.find(' ') != -1:
        print('Too many worlds..')
        continue
    if word in newList:
        print('Already has this word')
        continue
    newList.append(word)
    print(newList)
    
