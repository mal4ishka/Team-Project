class NotesSearch:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        self.notes.append({"title": title, "content": content})
        print(f'Note "{title}" added.')

    def search_notes(self, keyword):
        matching_notes = []
        for note in self.notes:
            if keyword.lower() in note["title"].lower() or keyword.lower() in note["content"].lower():
                matching_notes.append(note)

        if not matching_notes:
            print(f'No notes found with the keyword "{keyword}".')
        else:
            print(f'Search results for the keyword "{keyword}":')
            for note in matching_notes:
                print(f'--- {note["title"]} ---\n{note["content"]}\n')