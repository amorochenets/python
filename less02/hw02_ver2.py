print('Task #1\n')
while True :
    s = input('Please enter you string: ')
    if  len(s) >= 3:
        print('',s[2],s[-1],s[0:5],s[:-2],s[::2],s[1::2],s[::-1],s[::-2],len(s),sep='\n -- ')
        break
    else:
        print('String can\'t be empty and should content at less 3 symbols!\n')
print('Task #2:\n')
while True :
    l = input('Please enter you string: ')
    if len(l) > 0:
        lr = l[(len(l)+1)//2:] + l[:(len(l)+1)//2]
        print(lr)
        break
    else:
        print('String can\'t be empty!\n')
print('Task #3:\n')
while True :
    n = input('Please enter you string: ')
    if  len(n) == 0:
        print('String can\'t be empty!\n')
    elif n.find(' ') > 0 and n.count(' ') == 1:
        m = n.split()
        m = m[1] + ' ' + m[0]
        print(m)
        break
    else:
        print('String should contain two words separated with one space!')
