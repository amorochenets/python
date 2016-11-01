# !/usr/bin/env python3
# coding UTF-8


def file2set(file_name):
    '''
    :param file_name: file name for read
    :return: set of unical words
    '''
    open_file = open(file_name)
    new_set = list(open_file.read().split())
    counter = 0
    for word in new_set:
        if word[0] in '!,./-':
            new_set[counter] = word[1:]
        if word[-1] in '!,./-':
            new_set[counter] = word[:-1]
        counter += 1
    open_file.close()
    new_set = set(new_set)
    return new_set

newSet1 = file2set('file1.txt')
print(newSet1)

