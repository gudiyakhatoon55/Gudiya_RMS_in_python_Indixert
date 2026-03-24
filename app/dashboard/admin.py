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

            if not choice.isdigit():
                print("Invaild input")
                continue
            choice = int(choice)   

            if choice == 1:
                user_obj.add_staff()

            elif choice == 2:
                break
            else:
                print("Invalid choice")

    def menu_panel(self, menu_obj):

        while True:

            print("\n--- Menu Management ---")
            print("1 Add Item")
            print("2 View Item")
            print("3 Delete Item")
            print("4 Back")

            choice = input("Enter choice: ")

            if not choice.isdigit():
                continue

            choice = int(choice)

            if choice == 1:
                menu_obj.add_item()

            elif choice == 2:
                menu_obj.view_menu()

            elif choice == 3:
                menu_obj.delete_item()

            elif choice == 4:
                break