#The birthday greeting program.
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

input_name = input('Please input your name: ')
input_age = int(input('Please input your age: '))
print(f'Hello {input_name.capitalize()}, on your next birthday you’ll be {input_age + 1 } years')