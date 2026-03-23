from app.auth.signup import Signup
from app.auth.login import Login
from app.auth.manage_user import ManageUser

from app.dashboard.admin import AdminDashboard
from app.dashboard.staff import StaffDashboard

class Menu:

    def start(self):

        signup_obj = Signup()
        login_obj = Login()
        manage_user = ManageUser()
        admin_dashboard = AdminDashboard()
        staff_dashboard = StaffDashboard()

        while True:

            print("\n******* Restaurant Management System *******")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter choice: ").strip()

            if choice.isdigit():
                choice = int(choice)

            if choice == 1:
                signup_obj.signup()

            elif choice == 2:
                role = login_obj.login()

                if role == "admin":
                    admin_dashboard.start()

                elif role == "staff":
                    staff_dashboard.start()

            elif choice == 3:
                break

            else:
                print("Invalid choice")
            
       