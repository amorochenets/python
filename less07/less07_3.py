# !/usr/bin/env python3
# coding UTF-8

d = {(3, 'rew'): '4r5', 're': 13, 4: {1: 2, 3: 4, 5: 6}, (1, 4): 5, 'test': 2222}
for i in d:
    print('%s = %s' % (i, d[i]))

for i in d.values():
    print(i)
