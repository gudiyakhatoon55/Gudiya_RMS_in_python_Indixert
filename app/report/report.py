# # from app.database.filehandler import FileHandler

# # class Report:

# #     def __init__(self):
# #         self.file = FileHandler()

# #     def order_report(self):

# #         orders = self.file.read_file("orders.json")

# #         if not orders:
# #             print("No orders found ❌")
# #             return

# #         print("\n====== REPORT ======")


# #         for i, order in enumerate(orders, 1):
# #             print(f"\n--- Order {i} ---")

# #             total = 0

# #             for item in order:
# #                 name = item["name"]
# #                 qty = item["qty"]
# #                 price = item["price"]

# #                 amount = price * qty
# #                 total += amount

# #                 print(f"{name} x {qty} = ₹{amount}")

# #             print("Order Total:", total)
# #             grand_total += total

# #         print("\n====== FINAL TOTAL ======")
# #         print("Total: ", total)


# from app.database.filehandler import FileHandler

# class Report:

#     def __init__(self):
#         self.file = FileHandler()

#     def order_report(self):

#         orders = self.file.read_file("orders.json")

#         if not orders:
#             print("No orders found ❌")
#             return

#         print("\n====== ORDER REPORT ======")

#         total_sales = 0

#         for order in orders:  # 🔥 each order (list)
#             for item in order:  # 🔥 each item
#                 amount = item["price"] * item["qty"]
#                 total_sales += amount

#                 print(item["name"], "x", item["qty"], "=", amount)

#         print("----------------------")
#         print("Total Sales:", total_sales)


from app.database.filehandler import FileHandler
from datetime import datetime

class Report:

    def __init__(self):
        self.file = FileHandler()

    def order_report(self):

        orders = self.file.read_file("orders.json")

        if not orders:
            print("No orders found ❌")
            return

        print("\n====== ORDER REPORT ======")

        total_sales = 0
        report_data = []

        for order in orders:
            for item in order:
                amount = item["price"] * item["qty"]
                total_sales += amount

                print(item["name"], "x", item["qty"], "=", amount)

                # 👉 JSON ke liye data store karo
                report_data.append({
                    "name": item["name"],
                    "qty": item["qty"],
                    "amount": amount
                })

        print("----------------------")
        print("Total Sales:", total_sales)

        # 🔥 REPORT SAVE KARO
        final_report = {
            "date": str(datetime.now()),
            "total_sales": total_sales,
            "items": report_data
        }

        reports = self.file.read_file("report.json")  # file read
        reports.append(final_report)                 # new add
        self.file.write_file("report.json", reports) # save

        print("Report saved successfully ✅")