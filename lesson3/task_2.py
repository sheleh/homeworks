#The valid phone number program.
#Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.
input_number = '0972656577'
if input_number.isdigit() and len(input_number) == 10:
    print(f'number is OK, intrernational phone number format is '
          f'+38({input_number[:3]}) {input_number[3:6]} {input_number[6:8]} {input_number[8:10]}')
else: print('wrong number, please try again')

#variant2
numeric_status = False
len_status = False
alert_msg1 = ''  # this is a alert message 1
alert_msg2 = ''  # this is a alert message 2

if input_number.isdigit():
    numeric_status = True
else:
    alert_msg1 = 'Please use digits only'

if len(input_number) < 10:
    alert_msg2 = 'number is too less'
elif len(input_number) > 10:
    alert_msg2 = 'number is too big'
else:
    len_status = True

if numeric_status and len_status:
    print(f'number is OK, intrernational phone number format is '
        f'+38({input_number[:3]}) {input_number[3:6]} {input_number[6:8]} {input_number[8:10]}')
elif not numeric_status and not len_status:
    print(alert_msg1 + '\n' + alert_msg2)
elif not numeric_status:
    print(alert_msg1)
elif not len_status:
    print(alert_msg2)
else:
    print('something went wrong')
