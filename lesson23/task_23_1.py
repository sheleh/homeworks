import timeit
import time


# TASK 1
def to_power(x: int, exp: int) -> int:
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)


# TASK 2
def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) == 1:
        return True
    if len(looking_str) == 2:
        if looking_str[0] == looking_str[1]:
            return True
        else:
            return False
    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1: len(looking_str) - 1])
    return False


def is_palindrome2(string: str) -> bool:
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return is_palindrome2(string[1: len(string) - 1])
    return False


# TASK 3
def mult_(a: int, n: int) -> int:
    try:
        if n < 0:
            raise ValueError
        else:
            if n == 0:
                return n
            return a + mult_(a, n - 1)
    except ValueError as v_err:
        print(f'{type(v_err)}"This function works only with positive integers"')


print(mult_(10, 2))


# TASK4
def reverse(input_str: str) -> str:
    if len(input_str) == 1:
        return input_str
    return input_str[-1] + reverse(input_str[:len(input_str) - 1])


print(reverse('qwerty'))


# TASK 5
def sum_of_digits(digit_str: str) -> int:
    if len(digit_str) == 1:
        return int(digit_str)
    return int(digit_str[0]) + sum_of_digits(digit_str[1:])


# TASK6 "Recursion time difference"
def fib_rec(n: int) -> int:
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


t1 = timeit.Timer('fib_rec(33)', 'from __main__ import fib_rec')
print('first function ', t1.timeit(number=1), 'milliseconds')
t2 = timeit.Timer('fib_iter(33)', 'from __main__ import fib_iter')
print('second function ', t2.timeit(number=1), 'milliseconds')

code_to_test = '''
def fib_iter(n = 33):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
'''
# Другой вариаент подсчета Чтобы получить точное время,
# я приказал timeit() выполнить 100 циклов. Поэтому мне пришлось разделить вывод на 100,
# чтобы получить время выполнения только для одного цикла
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print('second function(2) ', elapsed_time, 'milliseconds')


start_time = time.time()
fib_iter(33)
print('second function(3) ', time.time() - start_time, 'milliseconds')
