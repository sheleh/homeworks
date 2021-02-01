#  Write a class TypeDecorators which has several methods for converting results of functions to a specified type
#  (if it's possible):
# Don't forget to use @wraps

from functools import wraps


class TypeDecorators:

    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                res = int(res)
            except ValueError:
                return f'cant assign to INT'
            return res
        return wrapper

    @classmethod
    def to_str(cls, func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                res = str(res)
            except ValueError:
                return f'cant assign to STRING'
            return res
        return wrapper

    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                res = bool(res)
            except ValueError:
                return f'cant assign to BOOLEAN'
            return res
        return wrapper

    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            try:
                res = float(res)
            except ValueError:
                return f'cant assign to FLOAT'
            return res
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


print(do_nothing('12345'))
print(type(do_nothing('43453453')))


@TypeDecorators.to_str
def do_something(integers: int):
    return integers


print(do_something(12345))
print(type(do_something(12345)))


@TypeDecorators.to_bool
def do_something_bool(string: bool):
    return string


print(do_something_bool(False))
print(type(do_something_bool(False)))


@TypeDecorators.to_float
def do_something__float(string: str):
    return string


print(do_something__float('12345'))
print(type(do_something__float('12345')))
