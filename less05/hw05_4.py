# !/usr/bin/env python3
# coding UTF-8
while True:
    number = input('Please, enter the integer number: ')
    if number.isdigit():
        result = 0
        for n in range(1, int(number)+1):
            result += n**2
        print(result)
        break
    else:
        print('ERR: Only integer digit should be entered!')
