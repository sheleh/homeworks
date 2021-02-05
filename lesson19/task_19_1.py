# File Context Manager class
# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers mentioned here:
import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.open_file = None
        self.counter_l = 0 + 1  # пустая строка в конце не считается
        self.counter_w = 0

    def __enter__(self):
        try:
            self.open_file = open(self.filename, self.mode)
        except Exception as err:
            logging.error(str(err))
        else:
            data = self.open_file.read()
            for _ in data:
                if _ == '\n':
                    self.counter_l += 1
                self.counter_w += 1
            self.open_file.seek(0)
            return self.open_file

    def __exit__(self, *args):
        print(f'File have {self.counter_w} symbols/ {self.counter_l} lines')
        try:
            self.open_file.close()
        except AttributeError:
            print('Эта ошибка в exit')


with File('foo.txt', 'r') as infile:
    print(infile)
    text = infile.readlines()
    print(f'text в конце {text}')