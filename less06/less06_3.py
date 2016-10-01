# !/usr/bin/env python3
# coding UTF-8
# import random
newList = [7, 4, 6, 5, 4, 6, 7, 4, 6, 7, 7, 6, 6, 4, 7]

# for num in range(15):
#     newList.append(random.randrange(4, 8))
print(newList)
addList = []
flag = None
# for i in newList:
#     if i != flag:
#         addList.append(i)
#     flag = i
# print(addList)
i = 0
lengz = len(newList)
while i < lengz:
    if newList[i] == flag:
        newList.pop(i)
        print(flag)
    else:
        print('---')
        i += 1
    flag = newList[i]
    lengz = len(newList)
print(newList)
