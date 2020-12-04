#Extracting numbers.
#Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
#Constraint: use only while loop for iteration


x = 1
i = 0
range_len = 100
num_list = []
res_list = []

while x <= range_len:
    num_list.append(x)
    x += 1

while i < len(num_list):
    if num_list[i] % 7 == 0 and num_list[i] % 5 != 0:
        res_list.append(num_list[i])
    i += 1

print(f'In range from 1 to 100 divisible by 7 but not a multiple of 5 is : {res_list}')
