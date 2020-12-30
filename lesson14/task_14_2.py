#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
#def stop_words(words: list):
#    pass
#@stop_words(['pepsi', 'BMW'])
#def create_slogan(name: str) -> str:
#    return f"{name} drinks pepsi in his brand new BMW!"
#assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
import re

def stop_words(words):
    def replace_words(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for s_word in words:
                res = re.sub(s_word, '*', res)
            return res
        return wrapper
    return replace_words


@stop_words(['BMW', 'pepsi'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'

print(create_slogan('JOHN'))
