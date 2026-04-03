# from app.menu.view_menu import Menu
# from app.order.order import Order


# class StaffDashboard:

#     def __init__(self):
#         self.menu = Menu()
#         self.order = Order()
    

#     def start(self):
#         while True:

#             print("\n====== STAFF DASHBOARD ======")
#             print("1. View Menu")
#             print("2. Take Order")
#             print("3. Generate Bill")
#             print("4. Table Booking")
#             print("5. Logout")

#             choice = input("Enter choice: ").strip()

#             if choice == "1":
#                 self.menu.view_menu()

#             elif choice == "2":
#                 self.order.take_order()

#             elif choice == "3":
#                 self.billing.generate_bill()

#             elif choice == "4":
#                 self.booking.table_booking()

#             elif choice == "5":
#                 print("Logging out...")
#                 break

#             else:
#                 print("Invalid choice ")




from app.menu.view_menu import Menu
from app.order.order import Order


class StaffDashboard:

    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def start(self):
        while True:

            print("\n====== STAFF DASHBOARD ======")
            print("1. View Menu")
            print("2. Take Order")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.menu.view_menu()

            elif choice == "2":
                self.order.take_order()

            elif choice == "3":
                print("Logging out...")
                break

            else:
                print("Invalid choice")