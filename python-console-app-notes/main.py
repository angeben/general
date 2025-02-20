from users import actions

# User action
print("""
Available actions:
    - Register
    - Login
""")

action = actions.Actions()
actionInput = input("Choose the action that you want to execute: ")
if actionInput.lower() == "register":
    action.register()
elif actionInput.lower() == "login":
    action.login()