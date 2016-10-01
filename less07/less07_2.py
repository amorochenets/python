# !/usr/bin/env python3
# coding UTF-8
newFile = open('newFile.txt', 'w')
someList = ('Lorem ipsum dolor sit amet, Consectetur adipisicing elit, sed do Aiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse, cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non roident, sunt in culpa qui officia deserunt mollit anim id est laborum.').split()
for i in someList:
    if 'a' <= i[0].lower() <= 'f':
        print(i)
        newFile.write(i + '\n')
newFile.close()
