# Create a class method named `validate`, which should be called from the `__init__` method
# to validate parameter email, passed to the constructor.
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
from lesson24.task_24_1 import Stack


class Validate:
    forb_symbols = ["'", '"', '<', '>', '|', '{', '}', ':', ';',
                    chr(92), '/', ' ', '#', '?', '%', '^', '`', '(', ')']
    warning_symb = ['_', ',', '.', '-']
    warning_symb_domain = ['_', ',', '-']
    prefix = ''
    domain = ''
    status = False

    def __init__(self, email_str):
        c = 0  # @ counter
        self.email_str = email_str
        for ch in self.email_str:
            if ch == '@':
                c += 1
        if c == 1:
            self.status = True
        else:
            self.status = False
        self.email_str = self.email_str.split('@')
        self.prefix = self.email_str[0]
        self.domain = self.email_str[1]
        i = 0
        while i != len(self.prefix):
            # проверка на явно запрещенные символы
            if self.prefix[i] in self.forb_symbols:
                self.status = False
                break
            # проверка на warning символы
            elif self.prefix[i-1] in self.warning_symb and self.prefix[i] in self.warning_symb:
                self.status = False
                break
            i += 1
        i = 0
        # проверка на warning символы в начале и конце
        if self.prefix[0] in self.warning_symb or self.prefix[-1] in self.warning_symb:
            self.status = False
        # проверка на длинну префикса
        elif len(self.prefix) < 3 or len(self.prefix) > 64:
            self.status = False

        while i != len(self.domain):
            # проверка на явно запрещенные символы
            if self.domain[i] in self.forb_symbols:
                self.status = False
                break
            # проверка на warning символы
            elif self.domain[i-1] in self.warning_symb and self.domain[i] in self.warning_symb:
                self.status = False
                break
            i += 1
        # проверка на наличие точки в доменном имени
        if '.' not in self.domain:
            self.status = False
        # проверка на длинну доменного имени
        elif len(self.domain) < 3 or len(self.domain) > 256:
            self.status = False
        # проверка на warning символы в начале и конце
        elif self.domain[0] in self.warning_symb or self.domain[-1] in self.warning_symb:
            self.status = False
        # проверка на длину конечного доменного имени
        elif self.domain[-2] == '.':
            self.status = False

    def __repr__(self):
        return f'{self.email_str} {self.status}'

    def __str__(self):
        return self.__repr__()


print(Validate('vasya@gmail.com'))