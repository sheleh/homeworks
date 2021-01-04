# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
# "add called with 4, 5"
# #def logger(func):
# pass
# @logger
# def add(x, y):
#    return x + y

# @logger
# def square_all(*args):
#    return [arg ** 2 for arg in args]

def logger(func):

    def wrapper(*args):
        res = '(' + str(args[0])
        for v in args[1:]: res += ', ' + str(v)
        res += ')'
        res = f'Function {func.__name__} called with arguments {res} '
        return res
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(5,2))

print(square_all(4,7,3))


