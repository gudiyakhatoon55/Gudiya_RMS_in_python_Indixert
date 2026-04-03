from app.database.filehandler import FileHandler
import getpass


class Login:

    def __init__(self):
        self.file = FileHandler()

    def login(self):
        print("\n====== LOGIN ======")

        email = input("Enter Email: ")
        password = getpass.getpass("Enter Password: ")

        users = self.file.read_file("users.json")

        if not users:
            print("No users found! Please signup first ")
            return None

        for user in users:
            if user["email"] == email and user["password"] == password:
                print("Login successful ")
                return user.get("role", "staff")  

        print("Invalid email or password ")
        return None