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