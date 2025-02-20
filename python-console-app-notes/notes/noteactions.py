import notes.note as model

class NoteActions:
    def create(self, user):
        print("\nLet's create a new note")
        title = input("Introduce the title of the note: ")
        desc = input("Introduce the content of the note: ")

        note = model.Note(user[0], title, desc)
        savedNote = note.save()

        if savedNote[0] >= 1:
            print(f"\nThe note '{note.title}' has been saved!")
        else:
            print(f"\nSorry, the note could not be saved")

    def show(self, user):
        print(f"\nOk, {user[1]}. These are your notes:")
        note = model.Note(user[0])
        notes = note.list()
        for n in notes:
            print('\n######################################')
            print(n[2])
            print(n[3])
            print('######################################')

    def delete(self, user):
        title = input(f"\nOk, {user[1]}. Introduce the name of the note you want to delete: ")
        note = model.Note(user[0], title)
        deleteNote = note.delete()

        if deleteNote[0] >= 1:
            print(f"The note '{note.title}' has been deleted")
        else:
            print("The note could not be saved")