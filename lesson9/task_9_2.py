#Extend Phonebook application
#
#Functionality of Phonebook application:
#Add new entries
#Search by first name
#Search by last name
#Search by full name
#Search by telephone number
#Search by city or state
#Delete a record for a given telephone number
#Update a record for a given telephone number
#An option to exit the program
#The first argument to the application should be the name of the phonebook. Application should load JSON data,
# if it is present in the folder with application, else raise an error. After the user exits,
# all data should be saved to loaded JSON.
import json
def main(filename):
    try:
        with open(f'{filename}.json', 'r', encoding='utf-8') as data:
            phonebook = json.load(data)
    #phonebook = {'0972656577': ['dmytro', 'shelekhov', 'dru'], '0508763465': ['vasya', 'pupkin', 'kiev'],
    #         '076348723': ['olga ', 'petrova', 'odessa'], '0509056209': ['donald', 'trump', 'new york'],
    #         '0972656578': ['dmytro', 'perestukin', 'dru']}
    except FileNotFoundError:
        print('OOPS Database not found')
    #print(phonebook)
    choice = 0
    while choice != 9:
        choice = get_menu_choice()
        if choice == 1:
            add_entries(phonebook)
        elif choice == 2:
            search_by_first_name_(phonebook)
        elif choice == 3:
            search_by_last_name_(phonebook)
        elif choice == 4:
            search_by_full_name(phonebook)
        elif choice == 5:
            search_by_telephone_num(phonebook)
        elif choice == 6:
            search_by_city(phonebook)
        elif choice == 7:
            delete_by_number(phonebook)
        elif choice == 8:
            update_by_number(phonebook)
        elif choice == 9:
            save_exit(phonebook)
        elif choice == 10:
            pass

def get_menu_choice():
    print('#='*23)
    print('\t'*4 + 'PHONEBOOK ')
    print('#='*23 + '\n')
    print('1. Add new entries ')
    print('2. Search by first name')
    print('3. Search by last name')
    print('4. Search by full name')
    print('5. Search by telephone number')
    print('6. Search by city or state')
    print('7. Delete a record for a given telephone number')
    print('8. Update a record for a given telephone number')
    print('9. Save and exit')
    choice = int(input('Please enter your choice: '))
    while choice < 1 or choice > 9:
        choice = int(input('Please enter your choice: '))
    return choice
def add_entries(phonebook):
    first_name = input('please enter your first name: ').capitalize()
    last_name = input('please enter your last name: ').capitalize()
    tel_number = input('please enter your telephone number: ').capitalize()
    city_name = input('please enter your city name').capitalize()
    if tel_number not in phonebook:
        phonebook[tel_number] = [first_name, last_name, city_name]
    else:
        print(' This number is already in phonebook')

def search_by_telephone_num(phonebook):
    tel_number = input('Please enter a telephone num:')
    print(phonebook.get(tel_number, 'Not found'))
def search_by_first_name_(phonebook):
    status = 0
    first_name = input('please enter a first name: ').capitalize()
    for key, val in phonebook.items():
        if first_name in val:
            status = 1
            print(key)
            print(val)
    if status == 0:
        print(f'name {first_name} not found')
def search_by_last_name_(phonebook):
    status = 0
    last_name = (input('please enter a last name: ')).lower()
    for key, val in phonebook.items():
        if last_name in val:
            status = 1
            print(key)
            print(val)
    if status == 0:
        print(f'name {last_name} not found')
def search_by_full_name(phonebook):
    status = 0
    full_name = input('please enter a full name name: ').lower()
    full_name = full_name.split()
    first_name = full_name[0]
    last_name = full_name[1]
    for key,val in phonebook.items():
        if first_name and last_name in val:
            status = 1
            print(key)
            print(val)
    if status == 0:
        print(f'{first_name} {last_name} not found')
def search_by_city(phonebook):
    status = 0
    city_name = input('please enter a city name').lower()
    for key,val in phonebook.items():
        if city_name in val:
            status = 1
            print(key)
            print(val)
    if status == 0:
        print(f'City {city_name} not founded or no people in this city')
def delete_by_number(phonebook):
    number = input('Please enter a telephone number: ')
    if number in phonebook:
        del phonebook[number]
        print(f'Number {number} deleted successfully')
        print(phonebook)
    else :
        print(f'Number {number} not in phonebook')
def update_by_number(phonebook):
    number = input('Please enter a telephone number: ')
    if number in phonebook:
        print(phonebook[number])
        for value in phonebook[number]:
            print(value)

def save_exit(phonebook):
    with open('phonebook.json', 'w') as file_object:
        json.dump(phonebook, file_object)
#search_by_telephone_num(phonebook)
#search_by_first_name_(phonebook)
#search_by_full_name(phonebook)
#search_by_city()
#delete_by_number()
#get_menu_choice()
main('phoneboo')