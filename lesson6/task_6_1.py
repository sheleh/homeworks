#Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.


txt_str = input('Pleaase insert a text: ')
txt_str = txt_str.lower()
txt_dict = {}
symbols = ['.',',','!','?',':',';','(',')','{','}','/','@',
           '#','$','%','^','&','*','-','_','=','+']

for symbol in symbols:
    if symbol in txt_str:
        txt_str = txt_str.replace(symbol, ' ')
        print(symbol)
txt_str = txt_str.split()
print(txt_str)

for item in txt_str:
    if item in txt_dict:
        txt_dict[item] = txt_dict[item] + 1
    else:
        txt_dict[item] = 1

print(f'Unique words and count of them is: {txt_dict}')
