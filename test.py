
def checkio(number):
    if not int(number)%3 and not int(number)%5 :
        number = 'Fizz Buzz'
    elif not int(number)%3 :
        number = 'Fizz'
    elif not int(number)%5 :
        number = 'Buzz'  
    return str(number)
print(checkio(135))
