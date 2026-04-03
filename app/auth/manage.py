# from app.auth.signup import Signup
# from app.auth.login import Login
# from app.database.filehandler import FileHandler


# class User:

#     def __init__(self):
#         self.file = FileHandler()
#         self.signup = Signup()
#         self.login = Login()

#     def start(self):
#         while True:
#             print("\n====== Registration ======")
#             print("1. Signup")
#             print("2. Login")
#             print("3. Exit")

#             choice = input("Enter choice: ").strip()

#             if choice == "1":
#                 self.signup.register()

#             elif choice == "2":
#                 role = self.login.login()

#                 if role == "admin":
#                     print("Welcome Admin ")
#                     self.manage_menu()

#                 elif role == "staff":
#                     print("Welcome Staff ")

#                 else:
#                     print("Login failed ")

#                 break

#             else:
#                 print("Invalid choice")

    
#     def manage_menu(self):
#         while True:
#             print("\n====== Manage Users ======")
#             print("1. View Users")
#             print("2. Delete User")
#             print("3. Back")

#             choice = input("Enter choice: ").strip()

#             if choice == "1":
#                 self.view_users()

#             elif choice == "2":
#                 self.delete_user()

#             elif choice == "3":
#                 break

#             else:
#                 print("Invalid choice")

    
#     def view_users(self):
#         users = self.file.read_file("users.json")

#         if not users:
#             print("No users found!")
#             return

    
#         for i, user in enumerate(users, start=1):
#             print(f"{i}. {user['name']} | {user['email']} | {user.get('role','')}")

    
#     def delete_user(self):
#         users = self.file.read_file("users.json")

#         if not users:
#             print("No users!")
#             return

#         self.view_users()

#         choice = input("Enter user number: ").strip()

#         if not choice.isdigit():
#             print("Invalid input")
#             return

#         choice = int(choice)

#         if choice < 1 or choice > len(users):
#             print("Invalid choice")
#             return

#         removed_user = users.pop(choice - 1)

#         self.file.write_file("users.json", users)

#         print(f"User '{removed_user['name']}' deleted successfully ")





from app.auth.signup import Signup
from app.auth.login import Login
from app.dashboard.admin import AdminDashboard
from app.dashboard.staff import StaffDashboard


class User:

    def __init__(self):
        self.signup = Signup()
        self.login = Login()

    def start(self):
        while True:
            print("\n====== Registration ======")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.signup.register()

            elif choice == "2":
                role = self.login.login()

                if role == "admin":
                    print("Welcome Admin 👑")
                    AdminDashboard().start()

                elif role == "staff":
                    print("Welcome Staff 👨‍🍳")
                    StaffDashboard().start()

                else:
                    print("Login failed ❌")

            elif choice == "3":
                break

            else:
                print("Invalid choice")