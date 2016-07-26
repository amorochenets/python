#!/usr/bin/env python3
#coding UTF-8
from sys import argv
var1, var2 = int(argv[1]), int(argv[2])
if  var1 > var2 :
    var3 = var1 - var2
elif var1 < var2 :
    var3 = var1 + var2
else:
    var3 = var1
print(var3)
