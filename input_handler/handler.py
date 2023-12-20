from Classes.Record import Record
from Classes.AddressBook import AddressBook
from sort.sort import FileSorted
import pickle
import os
from Classes.Note import Note, PersonalNoteAssistant


def handler():
    wait = True
    print('Type ? for help')
    while wait:
        inquire = input()
        parser(inquire)
        if inquire == '?':
            print(man)
        elif inquire == 'exit':
            wait = False


def parser(inquire):
    if inquire == 'add_contact':
        record = Record()
        address_book.add_contact(record)
        make_dump()
    elif inquire == 'print_contacts':
        address_book.print_contacts()
    elif inquire == 'add_email':
        address_book.add_email()
        make_dump()
    elif inquire == 'add_birthday':
        address_book.add_birthday()
        make_dump()
    elif inquire == 'add_phone':
        address_book.add_phone()
        make_dump()
    elif inquire == 'delete_phone':
        address_book.delete_phone()
        make_dump()
    elif inquire == 'delete_contact':
        address_book.delete_contact()
        make_dump()
    elif inquire == 'search_contacts':
        address_book.search_contacts()
    elif inquire == 'add_note':
        address_book.add_note()
        make_dump()
    elif inquire == 'delete_note':
        address_book.delete_note()
        make_dump()
    elif inquire == 'delete_email':
        address_book.delete_email()
        make_dump()
    elif inquire == 'edit_name':
        address_book.edit_name()
        make_dump()
    elif inquire == 'search_birthdays':
        address_book.search_birthdays()
    elif inquire == 'sort_files':
        sorter = FileSorted()
        sorter.clean_folder()
    else:
        print('Something went wrong. Please try again')


def make_dump():
    with open(data_name, "wb") as f:
        pickle.dump(address_book, f)


data_name = 'data/data.bin'
dats_size = os.path.getsize(data_name)

if dats_size == 0:
    address_book = AddressBook()
else:
    with open(data_name, "rb") as file:
        address_book = pickle.load(file)

with open('man.txt', 'r') as fh:
    man = fh.read()
