from app.auth.manage_user import ManageUser
class AdminDashboard:

    def start(self):

        user_obj =ManageUser()

        while True:

            print("\n ======= Admin Dashboard =======")
            print("1 Add Staff")
            print("2 View Users")
            print("3 Delete User")
            print("4 Search User")
            print("5 Menu")
            print("6 Reports")
            print("7 Back")

            choice = input("Enter choice: ").strip()

            if choice.isdigit():
                choice = int(choice)   

            if choice == 1:
                user_obj.add_staff()

            elif choice == 2:
                user_obj.view_users()

            elif choice == 3:
                break
            else:
                print("Invalid choice")