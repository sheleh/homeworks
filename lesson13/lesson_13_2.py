#Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def auth_system():
    print('Welcome to the command system, please enter your password')

    def in_pass():
        passw = input(':')
        return passw

    def __auth(_passw):
        if _passw == '1111':
            print('Login successfully ')
            return True
            #do some code

    def not_auth():
        print('password not correct - please try again: ')
        return 'password not correct - please try again: '
    i = 0
    while i != 10:
        if __auth(in_pass()):
            break
        not_auth()
        i += 1



auth_system()