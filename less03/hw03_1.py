#!/usr/bin/env python3
#coding UTF-8
from sys import argv
if len(argv) > 3 :
    if int(argv[3]) == 0 or int(argv[3]) == 1:
        song_line = 'la'*int(argv[2]) + '\n'
        song = song_line * int(argv[1])
        if  int(argv[3]) == 0:
            song = song[:-1] + '.'
        elif int(argv[3]) == 1:
            song = song[:-1] + '!'
        print(song)
    else:
        print('ERR! 3rd argument should be \'0\' or \'1\'')
else:
    print('ERR! Please start script with the three arguments!')
