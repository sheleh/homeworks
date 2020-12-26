#Write a Python program to detect the number of local variables declared in a function.

def some_foo():
    a = 1
    b = 2
    c = 'qwerty'
    d = True


def got_func_attr_2(foo):
    print(f'Number of variables = {len(foo.__code__.co_varnames)}')

def got_func_attr(foo):
    print(f'Number of variables = {foo.__code__.co_nlocals}')

def main():

    #f = some_foo
    got_func_attr(some_foo)
    got_func_attr_2(some_foo)

main()