#  Exclusive common numbers.
#  Generate 2 lists with the length of 10 with random integers from 1 to 10,
#  and make a third list containing the common integers between the 2 initial lists without any duplicates.
#  Constraints: use only while loop and random module to generate numbers

from random import randint
i = 0
random_list_1 = []
random_list_2 = []
common_list = []


while len(random_list_1) != 10 and len(random_list_2) != 10:
    random_list_1.append(randint(1, 10))
    random_list_2.append(randint(1, 10))

while i < len(random_list_1):
    if random_list_1[i] in random_list_2 and random_list_1[i] not in common_list:
        common_list.append(random_list_1[i])
    i += 1
# Variant 2 ######
#x = 0
#while i < len(random_list_1):
#    print(f'l1:{random_list_1[i]}')
#    while x < len(random_list_2):
#        print(f'l2:{random_list_2[x]}')
#        if random_list_1[i] == random_list_2[x]:
#            if random_list_1[i] not in common_list:
#                common_list.append(random_list_2[x])
#        x += 1
#    x = 0
#    i += 1

print(f'Random list 1 is : {random_list_1}\n'
      f'Random list 2 is : {random_list_2}\n'
      f'Intersection is : {common_list}')
