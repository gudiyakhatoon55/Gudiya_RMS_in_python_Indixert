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