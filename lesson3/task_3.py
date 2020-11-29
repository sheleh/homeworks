#Write a program that has a variable with your name stored (in lowercase)
# and then asks for your name as input. The program should check if your input is equal to the stored name
# even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”,
# it should return True.
name = 'dmytro'
input_name = 'Dmytro'
if name == input_name.lower():
    print(f'right_name {name} is correct')
else: print('Wrong, please try again')


#  variant2
status = False
while not status:
    input_name2 = input('Please try to guess a name or press 0 to exit: ')
    if input_name2 == name.lower():
        print('right')
        status = True
        break
    elif input_name2 == '0':
        print('looser')
        break
    else:
        print('wrong! please try again')

