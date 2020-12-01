#The Guessing Game.
#Write a program that generates a random number between 1 and 10
# and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
status = False
while not status:
    user_choice = int(input('lets try to guess a number between 1 and 10: '))
    random_number = random.randint(1,10)
    if user_choice == random_number:
        print(f'Got it!!! {user_choice} is right choice')
        break
    else:
        print('Nope, lets try again')