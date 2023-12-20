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
        make_dump(book_name, address_book)
    elif inquire == 'print_contacts':
        address_book.print_contacts()
    elif inquire == 'add_email':
        address_book.add_email()
        make_dump(book_name, address_book)
    elif inquire == 'add_birthday':
        address_book.add_birthday()
        make_dump(book_name, address_book)
    elif inquire == 'add_phone':
        address_book.add_phone()
        make_dump(book_name, address_book)
    elif inquire == 'delete_phone':
        address_book.delete_phone()
        make_dump(book_name, address_book)
    elif inquire == 'delete_contact':
        address_book.delete_contact()
        make_dump(book_name, address_book)
    elif inquire == 'search_contacts':
        address_book.search_contacts()
    elif inquire == 'delete_email':
        address_book.delete_email()
        make_dump(book_name, address_book)
    elif inquire == 'edit_name':
        address_book.edit_name()
        make_dump(book_name, address_book)
    elif inquire == 'search_birthdays':
        address_book.search_birthdays()
    elif inquire == 'sort_files':
        sorter = FileSorted()
        sorter.clean_folder()
    elif inquire == 'add_note':
        notes.add_note()
        make_dump(notes_name, notes)
    elif inquire == 'print_notes':
        notes.print_notes()
    elif inquire == 'delete_note':
        notes.delete_note()
        make_dump(notes_name, notes)
    elif inquire == 'edit_note':
        notes.edit_note()
        make_dump(notes_name, notes)
    else:
        print('Something went wrong. Please try again')


def make_dump(name, object):
    with open(name, "wb") as f:
        pickle.dump(object, f)


book_name = 'data/book.bin'
book_size = os.path.getsize(book_name)

if book_size == 0:
    address_book = AddressBook()
else:
    with open(book_name, "rb") as book_file:
        address_book = pickle.load(book_file)


notes_name = 'data/notes.bin'
notes_size = os.path.getsize(notes_name)

if notes_size == 0:
    notes = PersonalNoteAssistant()
else:
    with open(notes_name, "rb") as notes_file:
        notes = pickle.load(notes_file)


with open('man.txt', 'r') as fh:
    man = fh.read()
