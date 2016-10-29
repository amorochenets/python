# !/usr/bin/env python3
# coding UTF-8


def file2set(file_name):
    '''
    :param file_name: file name for read
    :return: set of unical words
    '''
    open_file = open(file_name)
    new_set = set(open_file.read().split())
    open_file.close()
    return new_set

newSet1 = file2set('file1.txt')
newSet2 = file2set('file2.txt')
print(newSet1 & newSet2, newSet1.difference(newSet2), sep='\n')

