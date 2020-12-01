#Task 3
#Words combination
#Create a program that reads an input string and then creates and prints 5
# random strings from characters of the input string.
# *************** не интересное решение *************
#from random import randrange
#input_str = input('please input a word')
#i = 0
#result = ''
#while i != 5-1:
#    random_index = randrange(0, 5)
#    random_ch = input_str[random_index]
#    result += random_ch
#    i += 1
#print(result)
# ***************************************************


import random
user_str = input('please print a string: ')
i = 0
res_str = ''  # финальная строка
used_chars = ''  # строка куда мы собираем все ранее использованные буквы
while len(res_str) < len(user_str):
    random_index = random.randrange(0, len(user_str))  # находим случайный индекс
    rand_char = user_str[random_index]  # вычисляем нужную букву
    # если буква еще не встречалась или в слове больше 2х одинаковых букв(костыль :-))
    if used_chars.find(rand_char) == -1 or user_str.count(rand_char) > 1:
        res_str += rand_char
    used_chars += rand_char
    i += 1
print(f'Changed string is = {res_str}')
