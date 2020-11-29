# String manipulation
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
sample_string = 'november'
if len(sample_string) >= 2:
    res = sample_string[:2] + sample_string[-2:]
else:
    res = ''
print(f'first 2 letters of \'{sample_string}\' is \'{res}\'')
