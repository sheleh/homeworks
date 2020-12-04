#  The greatest number
#  Write a Python program to get the largest number from a list of random numbers with the length of 10
#  Constraints: use only while loop and random module to generate numbers

from random import randint
i = 0
random_list = []
biggest_num = 0

while len(random_list) != 10:
    random_list.append(randint(1, 100))

while i != 10:
    if biggest_num < random_list[i]:
        biggest_num = random_list[i]
    i += 1

print(f'Biggest number from list {random_list} is : {biggest_num}')
