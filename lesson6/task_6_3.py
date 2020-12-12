#Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j`
#is corresponding to `i` squared.

### Переделал задание
new_list = [(i, i*i) for i in range(1, 11)]
print(new_list)