# !/usr/bin/env python3
# coding UTF-8
someList = [1, 2, 3, 4, 0, 5, -5, 2, -4, 2, -2, -4, -6, -7, 2, -3, 0, 0, 0, 42, 1, 3, 4, 6, -53, 53, 3, 0]
countZero = 0
countNegative = 0
countPositive = 0
for num in someList:
    if num > 0:
        countPositive += 1
    elif num < 0:
        countNegative += 1
    else:
        countZero += 1
print('Count of Zero: %s\nCount of Negative: %s\nCount of Positive: %s' % (countZero, countNegative, countPositive))
