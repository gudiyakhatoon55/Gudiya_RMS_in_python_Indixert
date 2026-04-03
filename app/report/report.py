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

        
                report_data.append({
                    "name": item["name"],
                    "qty": item["qty"],
                    "amount": amount
                })

        print("----------------------")
        print("Total Sales:", total_sales)


        final_report = {
            "date": str(datetime.now()),
            "total_sales": total_sales,
            "items": report_data
        }

        reports = self.file.read_file("report.json")  
        reports.append(final_report)                 
        self.file.write_file("report.json", reports) 

        print("Report saved successfully ✅")