from app.database.filehandler import FileHandler
from app.booking.booking import Booking
from app.billing.bill import Billing

class Order:

    def __init__(self):
        self.file = FileHandler()
        self.cart = []
        self.booking = Booking()


    def show_menu(self):
        menu = self.file.read_file("menu.json")   # 🔥 correct

        if not menu:
            print("Menu empty")
            return []

        print("\n------ MENU ------")
        for i, item in enumerate(menu, 1):
            print(i, item["name"], "-", item.get("price", ""))

        return menu


    def add_order(self):
        menu = self.show_menu()

        if not menu:
            return

        choice = input("Enter item number: ")

        if not choice.isdigit():
            print("Invalid input")
            return

        choice = int(choice)

        if choice < 1 or choice > len(menu):
            print("Invalid choice")
            return

        item = menu[choice - 1]

        
        if "half_price" in item:
            print("1. Half")
            print("2. Full")

            type_choice = input("Choose (1/2): ")

            if type_choice == "1":
                price = item["half_price"]
                size = "Half"
            elif type_choice == "2":
                price = item["full_price"]
                size = "Full"
            else:
                print("Invalid choice")
                return
        else:
            price = item["price"]
            size = "Full"

        qty = input("Enter quantity: ")

        if not qty.isdigit():
            print("Invalid quantity")
            return

        self.cart.append({
            "name": item["name"],
            "size": size,
            "price": price,
            "qty": int(qty)
        })

        print("Item added successfully ✅")

    def view_order(self):
        if not self.cart:
            print("No order yet")
            return

        print("\n------ YOUR ORDER ------")
        total = 0

        for i, item in enumerate(self.cart, 1):
            amount = item["price"] * item["qty"]
            total += amount
            print(f"{i}. {item['name']} ({item['size']}) x {item['qty']} = {amount}")

        print("Total:", total)


    def remove_order(self):
        if not self.cart:
            print("No order to remove")
            return

        self.view_order()

        choice = input("Enter item number to remove: ")

        if not choice.isdigit():
            print("Invalid input")
            return

        choice = int(choice)

        if choice < 1 or choice > len(self.cart):
            print("Invalid choice")
            return

        removed = self.cart.pop(choice - 1)
        print(f"{removed['name']} removed ❌")

    
    def update_order(self):
        if not self.cart:
            print("No order to update")
            return

        self.view_order()

        choice = input("Enter item number to update: ")

        if not choice.isdigit():
            print("Invalid input")
            return

        choice = int(choice)

        if choice < 1 or choice > len(self.cart):
            print("Invalid choice")
            return

        new_qty = input("Enter new quantity: ")

        if not new_qty.isdigit():
            print("Invalid quantity")
            return

        self.cart[choice - 1]["qty"] = int(new_qty)

        print("Order updated ✅")

    
    def take_order(self):
        while True:
            print("\n====== ORDER SYSTEM ======")
            print("1. Add Order")
            print("2. View Order")
            print("3. Update Order")
            print("4. Remove Order")
            print("5. Finish")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_order()

            elif choice == "2":
                self.view_order()

            elif choice == "3":
                self.update_order()

            elif choice == "4":
                self.remove_order()

            elif choice == "5":
                print("\nFinal Order:")
                self.view_order()

                
                orders = self.file.read_file("orders.json")
                orders.append(self.cart)
                self.file.write_file("orders.json", orders)

                
                bill = Billing()
                bill.generate_bill(self.cart)

            
                book = input("\nDo you want to book table? (yes/no): ").lower()

                if book == "yes":
                    self.booking.table_booking()
                else:
                    print("Order completed")

                self.cart = []
                break

            else:
                print("Invalid choice")