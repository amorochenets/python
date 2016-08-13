# !/usr/bin/env python3
# coding UTF-8
someList = [1, 3, 864, 234234, 42, 'sd', 'asdsa', 313, 'qdsa', 23, 234, 'dff22', '23efaf']
strList = []
numList = []
for elem in someList:
    if str(elem).isnumeric():
        numList.append(elem)
    else:
        strList.append(elem)
print(strList, numList, sep='\n')