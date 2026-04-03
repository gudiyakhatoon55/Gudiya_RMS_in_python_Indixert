from app.database.filehandler import FileHandler
from datetime import datetime, timedelta


class Booking:

    def __init__(self):
        self.file = FileHandler()
        self.slots = ["9-12", "12-3", "3-6"]
        self.total_tables = 10

    
    def is_valid_date(self, date_str):
        try:
            booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            today = datetime.today().date()

            if booking_date < today:
                print("Past date allowed nahi ❌")
                return False

            if booking_date > today + timedelta(days=10):
                print("Max 10 din tak hi booking allowed ❌")
                return False

            return True

        except:
            print("Invalid date format (YYYY-MM-DD)")
            return False


    def get_available_tables(self, date, slot):
        bookings = self.file.read_file("booking.json")

        booked_tables = [
            b["table"] for b in bookings
            if b["date"] == date and b["slot"] == slot
        ]

        available = [
            t for t in range(1, self.total_tables + 1)
            if t not in booked_tables
        ]

        return available

    def book_table(self):
        name = input("Enter customer name: ")
        date = input("Enter date (YYYY-MM-DD): ")

        if not self.is_valid_date(date):
            return

        print("\nAvailable Sets:")
        for i, set in enumerate(self.sets, 1):
            print(i, set)

        choice = input("Choose slot: ")

        if not choice.isdigit():
            print("Invalid input")
            return

        choice = int(choice)

        if choice < 1 or choice > len(self.slots):
            print("Invalid choice")
            return

        set = self.sets[choice - 1]

        available_tables = self.get_available_tables(date, set)

        if not available_tables:
            print("No table available for this slot ❌")
            return

        print("Available Tables:", available_tables)

        table_choice = input("Choose table number: ")

        if not table_choice.isdigit():
            print("Invalid input")
            return

        table_choice = int(table_choice)

        if table_choice not in available_tables:
            print("Table not available ❌")
            return

        bookings = self.file.read_file("booking.json")

        bookings.append({
            "name": name,
            "date": date,
            "set": set,
            "table": table_choice
        })

        self.file.write_file("booking.json", bookings)

        print(f"Table {table_choice} booked successfully ✅")


    def view_booking(self):
        bookings = self.file.read_file("booking.json")

        if not bookings:
            print("No bookings found")
            return

        print("\n------ BOOKINGS ------")
        for i, b in enumerate(bookings, 1):
            print(i, b["name"], "|", b["date"], "|", b["slot"], "| Table:", b["table"])


    def cancel_booking(self):
        bookings = self.file.read_file("booking.json")

        if not bookings:
            print("No booking to cancel")
            return

        self.view_booking()

        choice = input("Enter booking number to cancel: ")

        if not choice.isdigit():
            print("Invalid input")
            return

        choice = int(choice)

        if choice < 1 or choice > len(bookings):
            print("Invalid choice")
            return

        removed = bookings.pop(choice - 1)

        self.file.write_file("booking.json", bookings)

        print(f"Booking cancelled for {removed['name']} ❌")

    
    def table_booking(self):
        while True:
            print("\n====== TABLE BOOKING ======")
            print("1. Book Table")
            print("2. View Booking")
            print("3. Cancel Booking")
            print("4. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                self.book_table()

            elif choice == "2":
                self.view_booking()

            elif choice == "3":
                self.cancel_booking()

            elif choice == "4":
                break

            else:
                print("Invalid choice")