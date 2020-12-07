#Task 1
#Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.
txt_str = input('Pleaase insert a text')
txt_dict = {}
txt_str = txt_str.split()
symbols = [',', '.', '!', '?']
for item in txt_str:
    if (item[-1]) in symbols:
        item = item[:-1]

    if item in txt_dict:
        txt_dict[item] = txt_dict[item] + 1
    else:
        txt_dict[item] = 1

print(txt_dict)
