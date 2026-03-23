import uuid
from app.database.file_handler import read_users, write_user

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


class Signup:

    def signup(self):

        print("\n ------Signup------")

        user_id = str(uuid.uuid4())

        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input_password("Enter password: ")
        role = "staff"

        users = read_users()

        for user in users:
            if user["email"] == email:
                print("Email already exists")
                return role

        user = {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }

        write_user(user)

        print("Signup successful")

        return 