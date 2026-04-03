# from app.database.filehandler import FileHandler
# import getpass

# class Signup:

#     def __init__(self):
#         self.file = FileHandler()

#     def register(self):
#         name = input("Enter Name: ")
#         email = input("Enter Email: ")
        
    
#         password = getpass.getpass("Enter Password: ")
#         confirm_password = getpass.getpass("Confirm Password: ")

        
#         if password != confirm_password:
#             print("Passwords do not match!")
#             return

#         user = {
#             "name": name,
#             "email": email,
#             "password": password
#         }

#         self.file.append_file("users.json", user)

#         print("Signup Successfully!")



from app.database.filehandler import FileHandler
import getpass


class Signup:

    def __init__(self):
        self.file = FileHandler()

    def register(self):
        print("\n====== SIGNUP ======")


        name = input("Enter Name: ")
        email = input("Enter Email: ")

        password = getpass.getpass("Enter Password: ")
        confirm_password = getpass.getpass("Confirm Password: ")

        if password != confirm_password:
            print("Passwords do not match ")
            return

        users = self.file.read_file("users.json")

    
        for user in users:
            if user["email"] == email:
                print("Email already exists ")
                return

    
        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "role": "staff"
        }

        users.append(new_user)
        self.file.write_file("users.json", users)

        print("Signup successful ✅ (Role: staff)")