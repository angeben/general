import users.user as model
import notes.noteactions as noteactions

class Actions:
    def register(self):
        print("Let's register your user!\n")
        name = input("What is your name: ")
        email = input("Introduce your email: ")
        password = input("Choose your password: ")

        user = model.User(name, email, password)
        register = user.register()

        if register[0] >= 1:
            print(f"Nice! Your user has been registered, {register[1].name}")
        else:
            print("Sorry, there was an error...")

    def login(self):
        print("Let's login")
        try:
            email = input("Introduce your email: ")
            password = input("Introduce your password: ")

            user = model.User('', email, password)
            login = user.login()
            if email == login[2]:
                print(f"Welcome, {login[1]}")
                self.app_actions(login)

        except Exception as e:
            print(type(e), type(e).__name__)
            print(f"Incorrect login. Try again")
    
    def app_actions(self, user):
        print("""
        Available actions:
            - Create a new note (create)
            - Show your notes (show)
            - Delete a note (delete)
            - Exit (exit)
        """)
        actionInput = input("What do you want to do? ")
        parsedAction= actionInput.lower()
        noteAction = noteactions.NoteActions()
        if parsedAction == "create" or parsedAction == 'c':
            print("Create selected")
            noteAction.create(user)
            self.app_actions(user)
        elif parsedAction == "show" or parsedAction == 's':
            noteAction.show(user)
            self.app_actions(user)
        elif parsedAction == "delete" or parsedAction == 'd':
            noteAction.delete(user)
            self.app_actions(user)
        elif parsedAction == "exit" or parsedAction == 'e':
            print(f"See you soon, {user[1]}")
            exit()