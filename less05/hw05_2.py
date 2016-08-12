# !/usr/bin/env python3
# coding UTF-8
import random
# 1
for item in range(1, 15):
    print('%8.3f' % (random.random()*random.randrange(1,1000)))
print('--------')
# 2
for item in range(1, 15):
    print('%8d' % random.randrange(1,100, 2))
print('--------')
# 3
line = list(input('Please, enter some line: '))
random.shuffle(line)
print(''.join(line))
