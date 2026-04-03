from app.database.filehandler import FileHandler
from datetime import datetime


class Billing:

    def __init__(self):
        self.file = FileHandler()

    def generate_bill(self, cart):

        if not cart:
            print("No items to bill ❌")
            return

        print("\n========== BILL ==========")

        total = 0

        for item in cart:
            amount = item["price"] * item["qty"]
            total += amount
            print(f"{item['name']} x {item['qty']} = ₹{amount}")

        gst = total * 0.05
        grand_total = total + gst

        print("--------------------------")
        print(f"Subtotal: ₹{total}")
        print(f"GST (5%): ₹{gst:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")
        print("==========================")

        # 🔥 SAVE BILL IN JSON
        bills = self.file.read_file("bills.json")

        bills.append({
            "date": str(datetime.now()),
            "items": cart,
            "total": total,
            "gst": gst,
            "grand_total": grand_total
        })

        self.file.write_file("bills.json", bills)

        print("Bill saved successfully ✅")