#Creating a dictionary.
#Create a function called make_country, which takes in a country’s name and capital as parameters.
#Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.
#names = {}
#k = 0
#answer_n = ''
#def make_country(country, capital_name):
#    names['name'] = country
#    names['capital'] = capital_name
#    return names
#def output(names_dict):
#    for key, value in names_dict.items():
#        print(key,value)
#while answer_n != 'n':
#    answer_n = input('Please type a country name :')
#    answer_c = input('Please type a capital name :')
#    make_country(answer_n,answer_c)
#    print(names)
#else:
#    print(output(names))
#names_dict = make_country('Uk', 'London')
my_dict = {}


def make_country(countrys_name, capital):
    my_dict = {'name': countrys_name, 'capital_name': capital}
    return my_dict


def output(my_dict):
    for key, value in my_dict.items():
        print(f'The {key} of country is: {value}')


res = make_country('UK', 'London')
output(res)




