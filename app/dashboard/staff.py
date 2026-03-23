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

            if choice.isdigit():
                choice = int(choice)


            if choice == 1:
                print("Order system coming soon")

            elif choice == 2:
                print("Billing system coming soon")

            elif choice == 3:
                break

            else:
                print("Invalid choice")