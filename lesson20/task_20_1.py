# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook. Application should load JSON data,
# if it is present in the folder with application, else raise an error. After the user exits,
# all data should be saved to loaded JSON.
import json


def main(filename='phonebook') -> None:
    try:
        with open(f'{filename}.json', 'r', encoding='utf-8') as data:
            phonebook = json.load(data)
    except FileNotFoundError:
        print('OOPS Database not found')
        phonebook = {}
    except UnboundLocalError:
        print('Database Error')

    choice = 0
    while choice != 9:
        choice = get_menu_choice()
        if choice == 1:
            add_entries(phonebook)
            input('Press ENTER to continue')
        elif choice == 2:
            search_by_first_name_(phonebook)
            input('Press ENTER to continue')
        elif choice == 3:
            search_by_last_name_(phonebook)
            input('Press ENTER to continue')
        elif choice == 4:
            search_by_full_name(phonebook)
            input('Press ENTER to continue')
        elif choice == 5:
            search_by_telephone_num(phonebook)
            input('Press ENTER to continue')
        elif choice == 6:
            search_by_city(phonebook)
            input('Press ENTER to continue')
        elif choice == 7:
            delete_by_number(phonebook)
            input('Press ENTER to continue')
        elif choice == 8:
            update_by_number(phonebook)
            input('Press ENTER to continue')
        elif choice == 9:
            save_exit(filename, phonebook)


def get_menu_choice() -> int:
    print('#='*23)
    print('\t'*4 + 'PHONEBOOK ')
    print('#='*23)
    print('1. Add new entries ')
    print('2. Search by first name')
    print('3. Search by last name')
    print('4. Search by full name')
    print('5. Search by telephone number')
    print('6. Search by city or state')
    print('7. Delete a record for a given telephone number')
    print('8. Update a record for a given telephone number')
    print('9. Save and exit')
    while True:
        try:
            choice = int(input('Please enter your choice: '))
        except ValueError:
            print('Incorrect input')
        else:
            if 1 <= choice <= 9:
                return choice
            print('Incorrect input')


def add_entries(phonebook: dict) -> dict:
    first_name = input('please enter first name: ').capitalize().strip()
    last_name = input('please enter last name: ').capitalize().strip()
    tel_number = input('please enter telephone number: ').strip()
    city_name = input('please enter city name: ').capitalize().title()

    if not first_name.isalpha() or not last_name.isalpha() or not tel_number.isdigit() or not city_name:
        print('Wrong input, please try again or DIE)')
        add_entries(phonebook)
    else:
        if tel_number not in phonebook:
            phonebook[tel_number] = [first_name, last_name, city_name]
            return phonebook
        else:
            print(' This number is already in phonebook')


def search_by_telephone_num(phonebook: dict) -> None:
    tel_number = input('Please enter a telephone num: ').strip()
    tel_number if tel_number.isdigit() is True else print('Incorrect input')
    res = phonebook.get(tel_number)
    search_output(tel_number, res[0], res[1], res[2]) if res else print('Not found')


def search_by_first_name_(phonebook: dict) -> None:
    status = False
    first_name = input('please enter a first name: ').capitalize()
    first_name if first_name.isalpha() is True else print('Incorrect input')
    for key, val in phonebook.items():
        if first_name in val:
            status = True
            search_output(key, val[0], val[1], val[2])
    if not status:
        print(f'name {first_name} not found')


def search_by_last_name_(phonebook: dict) -> None:
    status = False
    last_name = input('please enter a last name: ').capitalize()
    last_name if last_name.isalpha() is True else print('Incorrect input')
    for key, val in phonebook.items():
        if last_name in val:
            status = True
            search_output(key, val[0], val[1], val[2])
    if not status:
        print(f'name {last_name} not found')


def search_by_full_name(phonebook: dict) -> None:
    status = False
    full_name = input('please enter a full name: ')
    full_name = full_name.split()
    full_name[0].isalpha()
    full_name[1].isalpha()
    if full_name[0] and full_name[1]:
        first_name = full_name[0].capitalize()
        last_name = full_name[1].capitalize()
        for key, val in phonebook.items():
            if first_name in val and last_name in val:
                status = True
                search_output(key, val[0], val[1], val[2])
        if not status:
            print(f'{first_name} {last_name} not found')
    else:
        print('Incorrect input')


def search_by_city(phonebook: dict) -> None:
    status = False
    city_name = input('please enter a city name: ').capitalize()
    city_name if city_name.isalpha() is True else print('Incorrect input')
    for key, val in phonebook.items():
        if city_name in val:
            status = True
            search_output(key, val[0], val[1], val[2])
    if not status:
        print(f'City {city_name} not founded or no people in this city')


def delete_by_number(phonebook: dict) -> None:
    number = input('Please enter a telephone number: ')
    if number.isdigit() is True:
        if number in phonebook:
            del phonebook[number]
            print(f'Number {number} deleted successfully')
            print(phonebook)
        else:
            print(f'Number {number} not in phonebook')
    else:
        print('Incorrect input')


def update_by_number(phonebook: dict) -> dict:
    number = input('Please enter a telephone number: ')
    number if number.isdigit() is True else print('Incorrect input')
    res = phonebook.get(number)
    first_name = input(f'please update first name {res[0]} : ').capitalize().strip()
    last_name = input(f'please update last name: {res[1]} : ').capitalize().strip()
    city_name = input(f'please update city name: {res[2]} : ').capitalize().title()

    if not first_name.isalpha() or not last_name.isalpha() or not city_name:
        print('Wrong input)')
    else:
        phonebook[number] = [first_name, last_name, city_name]
        return phonebook


def save_exit(filename, phonebook: dict) -> None:
    with open(f'{filename}.json', 'w', encoding='utf-8') as file_object:
        json.dump(phonebook, file_object)
        print('Saved')


def search_output(phone: str, name: str, lastname: str, city: str) -> None:
    print('_-'*23)
    print(f'* Phone Number : {phone} * \n* Name : {name} * '
          f'\n* Lastname : {lastname} * \n* City : {city} *')
    print('_-' * 23)


main('phonebookk_')