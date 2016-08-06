# !/usr/bin/env python3
# coding UTF-8
import random
# list = [12, 33, 44, 55, 'sdf', 'sdf', 43, 3434, 551, '34d']
# while list :
#     print(list)
#     list.pop()
#
# list2 = 'qweqqefwg4efwbwrgewbfw few fwgw wethgwrf gewgew'
# while list2:
#     print(list2)
#     list2 = list2[:-1]
# i = 10
# while True:
#     print('In aquarium is %s fish' % i)
#     i -= 1
#     if i < 0:
#         break
someList = ['qwe','betqnb','wdbe','betw','nrtw','ntrwnc','dsb','qwer']
# i = 0
# while i < len(someList):
#     print(someList[i] + '!')
#     i += 1

# for elem in someList:
#     print(elem + '!')

# newString = 'qwe 12e31d3f'
# for j in newString:
#     print('%s!' % j)
# print('-----')
# for word in 'one', 'two', 'three':
#     for symbol in word:
#         print('| %s |' % symbol)
#     print('-----')

# for s in range(1, 2420, 333):
#     print(s, end=' ')
# print()
w = ''
i = 0
while w != 'World':
    l = random.shuffle(list('World'))
    # w = ''.join(l)
    print(l)
    i += 1
print(i)

