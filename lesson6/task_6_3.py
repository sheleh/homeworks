#Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j`
#is corresponding to `i` squared.

new_list = [{i for i in range(1,10 + 1)}, {sum( i**i for i in range(1,10 + 1))} ]
print(new_list)