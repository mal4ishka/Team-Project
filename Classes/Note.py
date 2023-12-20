class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags


class PersonalNoteAssistant:
    def __init__(self):
        self.notes = []

    def add_note(self, text, tags):
        note = Note(text, tags)
        self.notes.append(note)

    def edit_note(self, index, new_text, new_tags):
        if 0 <= index < len(self.notes):
            self.notes[index].text = new_text
            self.notes[index].tags = new_tags
        else:
            print("Invalid index")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
        else:
            print("Invalid index")

    def search_notes_by_tag(self, tag):
        matching_notes = [note for note in self.notes if tag in note.tags]
        return matching_notes

    def display_notes(self):
        for i, note in enumerate(self.notes):
            print(f"Note {i + 1}:")
            print(f"Text: {note.text}")
            print(f"Tags: {', '.join(note.tags)}")
            print("---------------")

    #  create personal assistant"

    # assistant = PersonalAssistant()

    def note_processing(self):

        print("\n Please enter your choice!")
        print("1. Add note")
        print("2. Modify note")
        print("3. Delete note")
        print("4. Search note by tag")
        print("5. Print all notes")
        print("6. Exit")

        choice = input("Select your option: ")

        if choice == "1":
            text = input("Input note: ")
            tags = input("Input tags separated by comma: ").split(", ")
            self.add_note(text, tags)

        elif choice == "2":
            index = int(input("Enter the note number for edit: ")) - 1
            new_text = input("Enter the new text for the note: ")
            new_tags = input("Enter all tags separated by comma: ").split(", ")
            self.edit_note(index, new_text, new_tags)

        elif choice == "3":
            index = int(input("Enter the number of the note to delete: ")) - 1
            self.delete_note(index)

        elif choice == "4":
            tag = input("Input tag for the search: ")
            matching_notes = self.search_notes_by_tag(tag)
            if matching_notes:
                print("Notes found:")
                for note in matching_notes:
                    print(f"Text: {note.text}")
                    print(f"Tags: {', '.join(note.tags)}")
            else:
                print("Note with this tag is not found.")

        elif choice == "5":
            self.display_notes()

        elif choice == "6":
            pass
        else:
            print("Incorrect input. Try again!")