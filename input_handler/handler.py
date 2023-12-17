from Classes.Field import Field
from Classes.Name import Name
from Classes.Phone import Phone
from Classes.Birthday import Birthday
from Classes.Record import Record
from Classes.AddressBook import AddressBook


def handler():
    wait = True
    print('Type ? for help')
    while wait:
        inquire = input()
        response = parser(inquire)
        if response == man:
            print(man)
        if response == 'exit':
            wait = False


def parser(inquire):
    if inquire == '?':
        return OPERATIONS[inquire]
    elif inquire == 'add_contact':
        record = Record()
        address_book.add_contact(record)
    elif inquire == 'print_contacts':
        address_book.print_contacts()
    elif inquire == 'add_email':
        address_book.add_email()
    elif inquire == 'add_birthday':
        address_book.add_birthday()
    elif inquire == 'add_phone':
        address_book.add_phone()
    elif inquire == 'delete_phone':
        address_book.delete_phone()
    elif inquire == 'delete_contact':
        address_book.delete_contact()
    elif inquire == 'search_contacts':
        address_book.search_contacts()
    elif inquire == 'add_note':
        address_book.add_note()
    elif inquire == 'delete_note':
        address_book.delete_note()


def terminate(inquire):
    return 'exit'


address_book = AddressBook()

with open('man.txt', 'r') as fh:
    man = fh.read()


OPERATIONS = {
    'exit': terminate,
    '?': man,
    'add_contact': Record,
}