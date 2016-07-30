#!/usr/bin/env python3
#coding UTF-8
#1
number = 179**10
new_str = str(number)*4
result = round(int(new_str)**(1/10), 4)
print(result)
#2
number2 = '179'*50 + '.' + '179'*50
result2 = float(number2)**2
print(result2)