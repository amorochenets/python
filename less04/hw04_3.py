#!/usr/bin/env python3
#coding UTF-8
while True :
    num = input('Please enther the nubmer: ')
    if num != '' and num[0] == '-' :
        num1 = num[1:]
    else: 
        num1 = num
    if num1.rfind('.') != -1 :
        num1 = num1[:num1.rfind('.')] + num1[num1.rfind('.')+1:]˜
    if num1.isdigit() :
        if float(num) > 0 :
            print('Res is +')
        elif float(num) < 0 :
            print('Res is -')
        else:
            print('Res is 0')
        break
    else: 
        print('ERR! Value is not a number!')
        
 