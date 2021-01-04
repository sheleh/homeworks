#Custom exception
#Create your custom exception named `CustomException`,
# you can inherit from base Exception class, but extend its functionality
# to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

#class CustomException(Exception):

#def __init__(self, msg):

class CustomException(Exception):
    def __init__(self, message):
        self.msg = str(message)
        with open('logs.txt', 'w+') as fo:
            fo.write(self.msg)


def raiser():
    try:
        raise IndexError
    ## Вызвал родительский класс т.к. не выходит вызвать Customexpression и в него же передать сообщение
    ## Возможно следует создать еще один класс для этих целей (лишний раз нагрузит код)
    except Exception as e:
        msg = "Oops!", e.__class__, "occurred."
        CustomException(msg)


raiser()