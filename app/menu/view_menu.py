# # from app.database.filehandler import FileHandler

# # class Menu:

# #     def __init__(self):
# #         self.file = FileHandler()

# #     def view_menu(self):
# #         menu = self.file.read_file("menu.json")

# #         if not menu:
# #             print("Menu empty hai")
# #             return

# #         print("Menu:")

# #         for item in menu:
# #             print(item["name"], "-", item["price"])






# from app.database.filehandler import FileHandler


# class Menu:

#     def __init__(self):
#         self.file = FileHandler()


#     def view_menu(self):
#         menu = self.file.read_file("menu.json")

#         if not menu:
#             print("Menu empty hai")
#             return

#         print("\nMenu:")
#         for i, item in enumerate(menu, start=1):
#             print(i, item["name"], "-", item["price"])


#     def add_item(self):
#         name = input("Enter item name: ")
#         price = input("Enter price: ")

#         if not price.isdigit():
#             print("Invalid price")
#             return

#         price = int(price)

#         menu = self.file.read_file("menu.json")

#         menu.append({
#             "name": name,
#             "price": price
#         })

#         self.file.write_file("menu.json", menu)

#         print("Item added successfully")

    
#     def remove_item(self):
#         menu = self.file.read_file("menu.json")

#         if not menu:
#             print("Menu empty")
#             return

#         self.view_menu()

#         choice = input("Enter item number to delete: ")

#         if not choice.isdigit():
#             print("Invalid input")
#             return

#         choice = int(choice)

#         if choice < 1 or choice > len(menu):
#             print("Invalid choice")
#             return

#         removed = menu.pop(choice - 1)

#         self.file.write_file("menu.json", menu)

#         print(f"{removed['name']} removed successfully")

    
#     def update_item(self):
#         menu = self.file.read_file("menu.json")

#         if not menu:
#             print("Menu empty")
#             return

#         self.view_menu()

#         choice = input("Enter item number to update: ")

#         if not choice.isdigit():
#             print("Invalid input")
#             return

#         choice = int(choice)

#         if choice < 1 or choice > len(menu):
#             print("Invalid choice")
#             return

#         item = menu[choice - 1]

#         name = input(f"New name ({item['name']}): ") or item["name"]
#         price = input(f"New price ({item['price']}): ") or item["price"]

#         if isinstance(price, str) and price.isdigit():
#             price = int(price)

#         item["name"] = name
#         item["price"] = price

#         self.file.write_file("menu.json", menu)

#         print("Item updated successfully")

    
#     def menu_system(self):
#         while True:
#             print("\n====== MENU MANAGEMENT ======")
#             print("1. View Menu")
#             print("2. Add Item")
#             print("3. Remove Item")
#             print("4. Update Item")
#             print("5. Back")

#             choice = input("Enter choice: ")

#             if choice == "1":
#                 self.view_menu()

#             elif choice == "2":
#                 self.add_item()

#             elif choice == "3":
#                 self.remove_item()

#             elif choice == "4":
#                 self.update_item()

#             elif choice == "5":
#                 break

#             else:
#                 print("Invalid choice")




# from app.database.filehandler import FileHandler


# class Menu:

#     def __init__(self):
#         self.file = FileHandler()

    # def view_menu(self):
    #     menu = self.file.read_file("menu.json")

    #     if not menu:
    #         print("Menu empty")
    #         return

    #     print("\n"+"="*35)
    #     print(" Menu ")
    #     print("="*35)

    #     for i, item in enumerate(menu, 1):
    #         print(f"{i:>2}. {item['name']:<20} ₹{item['price']:>5}")

    #     print("="*35)


    # def add_item(self):
    #     name = input("Name: ")
    #     price = input("Price: ")

    #     if not price.isdigit():
    #         print("Invalid price")
    #         return

    #     menu = self.file.read_file("menu.json")

    #     menu.append({
    #         "name": name,
    #         "price": int(price)
    #     })

    #     self.file.write_file("menu.json", menu)

    # def view_menu(self):
    # menu = self.file.read_file("menu.json")

    # if not menu:
    #     print("Menu empty ❌")
    #     return

    # print("\n==============================================")
    # print("                 MENU")
    # print("==============================================")

    # for i, item in enumerate(menu, 1):
    #     print(f"{i:2}. {item['name']:<25} Half ₹{item['half_price']:<5} Full ₹{item['full_price']}")

    # print("==============================================")

    # def add_item(self):
    # name = input("Enter dish name: ").strip()

    # half = input("Enter Half price: ")
    # full = input("Enter Full price: ")

    # if not (half.isdigit() and full.isdigit()):
    #     print("Invalid price ❌")
    #     return

    # menu = self.file.read_file("menu.json")

    # # 🔥 Duplicate check
    # for item in menu:
    #     if item["name"].lower() == name.lower():
    #         print("Dish already exists ❌")
    #         return

    # menu.append({
    #     "name": name,
    #     "half_price": int(half),
    #     "full_price": int(full)
    # })

    # self.file.write_file("menu.json", menu)

    # print("Item added successfully ✅")

    # def remove_item(self):
    #     menu = self.file.read_file("menu.json")

    #     self.view_menu()
    #     i = int(input("Enter number: "))

    #     menu.pop(i - 1)
    #     self.file.write_file("menu.json", menu)

    # def update_item(self):
    #     menu = self.file.read_file("menu.json")

    #     self.view_menu()
    #     i = int(input("Enter number: "))

    #     menu[i - 1]["name"] = input("New name: ")
    #     menu[i - 1]["price"] = int(input("New price: "))

    #     self.file.write_file("menu.json", menu)

    # def menu_system(self):
    #     while True:
    #         print("\n1 View")
    #         print("2 Add")
    #         print("3 Remove")
    #         print("4 Update")
    #         print("5 Back")

    #         c = input("Choice: ")

    #         if c == "1":
    #             self.view_menu()
    #         elif c == "2":
    #             self.add_item()
    #         elif c == "3":
    #             self.remove_item()
    #         elif c == "4":
    #             self.update_item()
    #         elif c == "5":
    #             break


from app.database.filehandler import FileHandler


class Menu:

    def __init__(self):
        self.file = FileHandler()

    # ✅ VIEW MENU (Half/Full support)
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

    # ✅ ADD ITEM
    def add_item(self):
        name = input("Enter dish name: ").strip()

        half = input("Enter Half price: ")
        full = input("Enter Full price: ")

        if not (half.isdigit() and full.isdigit()):
            print("Invalid price ❌")
            return

        menu = self.file.read_file("menu.json")

        # 🔥 Duplicate check
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

    # ✅ REMOVE ITEM
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

    # ✅ UPDATE ITEM
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

    # ✅ MENU SYSTEM
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