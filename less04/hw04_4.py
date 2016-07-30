#!/usr/bin/env python3
#coding UTF-8
while True :
    num = input('Please enther an integer nubmer: ')
    symb = 1
    res = 1
    if num != '' and num[0] == '-' :
        num = num[1:]
        symb = -1
    if num.isdigit() :
        num = int(num)
        couner = 1
        while couner <= num :
            res *= couner
            couner += 1
        if num % 2 == 1 and symb == -1:
            res = -1 * res 
        print('Res = ', res)
        break
    else :
        print('ERR! Value is not an integer number!')