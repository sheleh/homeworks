# Manipulate strings.
firstname = 'dmytro'
lastname = 'shelekhov'
# Transformation the first symbol into the capital
firstname = firstname.capitalize()
lastname = lastname[0].upper() + lastname[1:]
string = 'Hello ' + firstname + ' ' + lastname + '! Get up and do a job'
print(string)
