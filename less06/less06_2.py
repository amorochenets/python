# !/usr/bin/env python3
# coding UTF-8
someList = ['qwq', 'qwww', 'edfre', 'f', '23f43v', 'sds', 'asdsa', '313', 'qdsa', 'vv3weffwev']
counter = 0
newList = []
for elem in someList:
    if len(str(elem)) >=2:
        if elem[0] == elem[-1]:
            counter += 1
            newList.append(elem)
print('result: %s\nNew list: %s' % (counter, newList))

