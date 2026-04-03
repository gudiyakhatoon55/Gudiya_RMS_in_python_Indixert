from app.database.filehandler import FileHandler


class Menu:

    def __init__(self):
        self.file = FileHandler()


    def view_menu(self):
        menu = self.file.read_file("menu.json")

        if not menu:
            print("Menu empty ❌")
            return

        print("\n==============================================")
        print("                   MENU")
        print("==============================================")

        for i, item in enumerate(menu, 1):

            if isinstance(item, list):
                item = item[0]

            half = item.get("half_price")
            full = item.get("full_price")
            if half and full:
                print(f"{i:2}. {item['name']:<25} Half ₹{half:<5} Full ₹{full}")
            else:
                print(f"{i:2}. {item['name']:<25} Half ₹{item['half_price']:<5} Full ₹{item['full_price']}")

        print("==============================================")

    
    def add_item(self):
        name = input("Enter dish name: ").strip()

        half = input("Enter Half price: ")
        full = input("Enter Full price: ")

        if not (half.isdigit() and full.isdigit()):
            print("Invalid price ❌")
            return

        menu = self.file.read_file("menu.json")

    
        for item in menu:
            if item["name"].lower() == name.lower():
                print("Dish already exists ❌")
                return

        menu.append({
            "name": name,
            "half_price": int(half),
            "full_price": int(full)
        })

        self.file.write_file("menu.json", menu)

        print("Item added successfully ✅")

    
    def remove_item(self):
        menu = self.file.read_file("menu.json")

        if not menu:
            print("Menu empty ❌")
            return

        self.view_menu()

        choice = input("Enter number to delete: ")

        if not choice.isdigit():
            print("Invalid input ❌")
            return

        choice = int(choice)

        if choice < 1 or choice > len(menu):
            print("Invalid choice ❌")
            return

        removed = menu.pop(choice - 1)

        self.file.write_file("menu.json", menu)

        print(f"{removed['name']} deleted ✅")

    def update_item(self):
        menu = self.file.read_file("menu.json")

        if not menu:
            print("Menu empty ❌")
            return

        self.view_menu()

        choice = input("Enter number to update: ")

        if not choice.isdigit():
            print("Invalid input ❌")
            return

        choice = int(choice)

        if choice < 1 or choice > len(menu):
            print("Invalid choice ❌")
            return

        name = input("New name: ")
        half = input("New Half price: ")
        full = input("New Full price: ")

        if not (half.isdigit() and full.isdigit()):
            print("Invalid price ❌")
            return

        menu[choice - 1] = {
            "name": name,
            "half_price": int(half),
            "full_price": int(full)
        }

        self.file.write_file("menu.json", menu)

        print("Item updated successfully ✅")

    
    def menu_system(self):
        while True:
            print("\n====== MENU MANAGEMENT ======")
            print("1 View Menu")
            print("2 Add Item")
            print("3 Remove Item")
            print("4 Update Item")
            print("5 Back")

            choice = input("Choice: ")

            if choice == "1":
                self.view_menu()

            elif choice == "2":
                self.add_item()

            elif choice == "3":
                self.remove_item()

            elif choice == "4":
                self.update_item()

            elif choice == "5":
                break

            else:
                print("Invalid choice ❌")