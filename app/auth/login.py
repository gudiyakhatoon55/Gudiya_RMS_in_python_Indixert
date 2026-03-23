from app.database.file_handler import read_users

import msvcrt

def input_password(prompt="Enter password: "):
    print(prompt, end="", flush=True)

    password = ""

    while True:
        char = msvcrt.getch()

        if char == b'\r':
            print()
            break
        elif char == b'\x08':
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += char.decode()
            print("*", end="", flush=True)

    return password

class Login:

    def login(self):

        print("\n ------Login------")

        email = input("Enter email: ").lower()
        password = input_password("Enter password: ")

        users = read_users()

        for user in users:

            if user["email"] == email and user["password"] == password:

                print("Login successful")
                print("Welcome", user["username"])

                return user["role"]  

        print("Invalid email or password")
        return 
