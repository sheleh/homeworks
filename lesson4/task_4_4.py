#The math quiz program
#Write a program that asks the answer for a mathematical expression,
#checks whether the user is right or wrong, and then responds with a message accordingly.
import random
operators = '+-/*'
random_operator = operators[random.randint(0,3)]
arg1 = random.randint(1,10)
arg2 = random.randint(1,10)
user_answer = ''
res = ''

if random_operator == '+':
    res = arg1 + arg2
elif random_operator == '-':
    res = arg1 - arg2
elif random_operator == '/':
    res = arg1 / arg2
    res = round(res, 1)
elif random_operator == '*':
    res = arg1 * arg2


while user_answer != res:
    if type(res) is float:
        print('Please use \'.\' NOT \',\'')
        user_answer = float(input(f'{arg1}  {random_operator}  {arg2} = '))
    else:
        user_answer = int(input(f'{arg1}  {random_operator}  {arg2} = '))

    if user_answer == res:
        print('RIGHT!!!')
    else:
        print('WRONG, please try again')

