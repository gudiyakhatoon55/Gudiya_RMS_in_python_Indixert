from app.auth.manage_user import ManageUser

class StaffDashboard:

    def start(self):


        while True:

            print("\n====== Staff Dashboard ======")
            print("1 View Menu")
            print("2 Take Order")
            print("3 Billing")
            print("4 Table Booking")
            print("5 Back")

            choice = input("Enter choice: ").strip()

            if not choice.isdigit():
                print("Invalid input")
                continue
            choice = int(choice)


            print("Invalid choice")