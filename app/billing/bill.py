from datetime import datetime

class Billing:

    def generate_bill(self, cart):

        if not cart:
            print("No items in cart ❌")
            return

        print("\n========== BILL ==========")
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("--------------------------")

        total = 0

        for item in cart:
            name = item["name"]
            price = item["price"]
            qty = item["qty"]

            amount = price * qty
            total += amount

            # print(f"{name} x {qty} = ₹{amount}")
            print(f"{item['name']} ({item['size']}) x {item['qty']} = ₹{amount}")

        print("--------------------------")

        # 💰 GST Calculation (5%)
        gst = total * 0.05
        grand_total = total + gst

        print(f"Subtotal: ₹{total}")
        print(f"GST (5%): ₹{gst:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")

        print("==========================")
        print("Thank you! Visit again 😊")