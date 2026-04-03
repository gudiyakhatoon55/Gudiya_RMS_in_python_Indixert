# from app.auth.manage import ManageUser
# from app.menu import Menu


# class AdminDashboard:

#     def __init__(self):
#         self.user = ManageUser()
#         self.menu = Menu()

#     def start(self):
#         while True:

#             print("\n====== ADMIN DASHBOARD ======")
#             print("1. Manage Users")
#             print("2. View Menu")
#             print("3. Add Menu Item")
#             print("4. Logout")

#             choice = input("Enter choice: ").strip()

#             if choice == "1":
#                 self.user.manage_menu()  

#             elif choice == "2":
#                 self.menu.view_menu()   

#             elif choice == "3":
#                 self.add_menu_item()     

#             elif choice == "4":
#                 print("Logging out...")
#                 break

#             else:
#                 print("Invalid choice ")

#     # ➕ Add Menu Item
#     def add_menu_item(self):
#         name = input("Enter item name: ")
#         price = input("Enter price: ")

#         if not price.isdigit():
#             print("Invalid price")
#             return

#         price = int(price)

#         from app.database.file_handler import FileHandler
#         file = FileHandler()

#         menu = file.read_file("menu.json")

#         menu.append({
#             "name": name,
#             "price": price
#         })

#         file.write_file("menu.json", menu)

#         print("Item added successfully ")





from app.menu.view_menu import Menu
from app.report.report import Report


class AdminDashboard:

    def __init__(self):
        self.menu = Menu()
        self.report = Report()

    def start(self):
        while True:

            print("\n====== ADMIN DASHBOARD ======")
            print("1. Manage Menu")
            print("2. Report")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.menu.menu_system()

            elif choice == "2":
                self.report.order_report()

            elif choice == "3":
                print("Logging out...")
                break

            else:
                print("Invalid choice")