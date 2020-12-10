# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

#################### Хотел провести вычисления в блоке  ELSE #######
# def input_numbers():
#    try:
#        a = int(input('Please enter a first number: '))
#        b = int(input('Please enter a second number: '))
#        if b == 0:
#            raise ZeroDivisionError
#        if type(a) != int and type(b) != int:
#            raise ValueError
#    except ValueError:
#        print('This is not a number, please try again')
#    except ZeroDivisionError:
#        print('Not a ZERO in second argument please')
#    except:
#        print('Houston, we have problem!!!')
#        raise
#    else:
#        res = (a*a) / b
#        print(res)
#
#
# input_numbers()
########## Реализовал подобие цикла до корректного ввода #################
#def input_num():
#    a = int(input('Please enter a first number: '))
#    b = int(input('Please enter a second number: '))
#    return a, b


#def check_num():
#    try:
#        a, b = input_num()
#        res = (a * a) / b
#        print(f'Result is : {res}')
#    except ValueError:
#        print('This is not a number, please try again')
#        check_num()
#    except ZeroDivisionError:
#        print('Not a ZERO in second argument please')
#        check_num()
#    except:
#        print('Houston, we have problem!!!')
#
#
# check_num()
def numbers():
    try:
        a = int(input('Please enter a first number: '))
        b = int(input('Please enter a second number: '))
        res = (a * a) / b
        print(f'Result is: {res}')
    except ValueError:
        print('This is not a number, please try again')
    except ZeroDivisionError:
        print('Not a ZERO in second argument please')
    except:
        print('Houston, we have problem!!!')
        raise
    else:
        print(f'I\'m in a else block and result is: {res}')


numbers()