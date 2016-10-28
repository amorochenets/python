# !/usr/bin/env python3
# coding UTF-8

deptCounter = {
    'adm': 14,
    'its': 7,
    'ops': 22,
    'pmo': 33,
    'qa': 65,
    'eng_mob': 42,
    'mgmt': 4,
    'hr': 16,
    'rec': 13,
    'rm': 28
}

def printDist(dist):
    print('Here is the list of departments:')
    print('-'*22)
    for key in dist:
        print('| %10s | %5s |' % (key, dist[key]))
        print('-' * 22)
numOfAll = 0
listOfDept = list(deptCounter.keys())
while True:
    print('Here is the list of departments: %s.' % ', '.join(listOfDept))
    deptName = input('Please enter dept for return number of people in dept (enter "all" for number of all people.): ')
    if deptName.lower() == 'all':
        if numOfAll == 0:
            for key in deptCounter:
                numOfAll += deptCounter[key]
        print('The number of all people in company is %s!' % numOfAll)
    elif deptName.lower() in listOfDept:
        print('The number of people in %s dept is %s!' % (deptName.lower(), deptCounter[deptName.lower()]))
    else:
        print('ERR! You are enter wrong value. PLease repeat!')
    breakPoint = input('Need to repeat? (Y/n): ')
    if breakPoint.lower() in ('n', 'no'):
        break
editTrigger = input('Enter to "Edit mode"? (y/N): ')
if editTrigger.lower() in ('y', 'yes'):
    while True:
        actionNumber = input('Please choose the number of action.\n#1 . Edit existing department;\n#2. Add new department.\n')
        if actionNumber == '1':
            while True:
                deptNameForEdit = input('Here is the list of departments: %s. Please enter dept for edit.\nD: ' % ', '.join(listOfDept))
                if deptNameForEdit.lower() in listOfDept:
                    deptCounter[deptNameForEdit] = int(input('Please enter new count of people in dept %s: ' %deptNameForEdit))
                else:
                    print('ERR! You are enter wrong value. PLease try again!')
                breakPoint = input('Need to repeat? (Y/n): ')
                if breakPoint.lower() in ('n', 'no'):
                    break
        elif actionNumber == '2':
            while True:
                newDept = input('Please enter new department: ')
                if newDept.lower() not in listOfDept:
                    deptCounter[newDept.lower()] = int(input('Please enter the number of people in dept: '))
                else:
                    print('This department already exist!')
                breakPoint = input('Need to add another dept? (Y/n): ')
                if breakPoint.lower() in ('n', 'no'):
                    break
        else:
            print('ERR! You are enter wrong value. PLease try again!')
        breakPoint = input('Exit from "Edit mode"? (y/N): ')
        if breakPoint.lower() in ('y', 'yes'):
            break
printDist(deptCounter)
