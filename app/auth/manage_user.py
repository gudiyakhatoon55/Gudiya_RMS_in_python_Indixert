import uuid
from app.database.file_handler import write_user, read_users

class ManageUser:

    def add_staff(self):

        user_id = str(uuid.uuid4())

        username = input("Enter staff name: ")
        email = input("Enter staff email: ")
        password = input("Enter password: ")

        users = read_users()

        for user in users:
            if user["email"] == email:
                print("Email already exists")
                return
        
        user = {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
            "role": "staff"
        }

        write_user(user)

        print("Staff added successfully")

    def view_users(self):

        users = read_users()

        for user in users:
            print(user)