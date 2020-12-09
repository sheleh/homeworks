#A simple calculator.
#Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(operator, *args):
    res = 0
    if operator == '+':
        for i in args:
            res += i
    elif operator == '-':
        for i in range(len(args)-1):
            print(i)
            if i == 0:
                res = args[0]
            res = res - args[i+1]
    elif operator == '*':
        for i in range(len(args)-1):
            print(i)
            if i == 0:
                res = args[0]
            res = res * args[i+1]

    return res
print(make_operation('+',7,6,-13,-5))