import home
import csv
from datetime import datetime

class OrderManagement:
    def __init__(self, menu_file, sales_file):
        self.orders = []
        self.menu = self.load_menu(menu_file)
        self.sales_file = sales_file

    def load_menu(self, menu_file):
        menu = {}
        with open(menu_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu[row['item']] = float(row['price'])  # Convert price to float
        return menu

    def place_order(self, item_name, quantity):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.sales_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, item_name, quantity, self.menu[item_name]])

        self.orders.append({'item': item_name, 'quantity': quantity})

        total_cost = 0
        print("\n------- Bill -------")
        for order in self.orders:
            item_name = order['item']
            quantity = order['quantity']
            item_cost = self.menu[item_name] * quantity
            print(f"{quantity} {item_name}(s) - ${item_cost:.2f}")
            total_cost += item_cost
        print(f"Total: ${total_cost:.2f}")
        return total_cost


def main():
    menu_file = 'menu.csv'
    sales_file = 'sales.csv'
    order_manager = OrderManagement(menu_file, sales_file)

    while True:
        print("\n----- Main Menu -----")
        print("1. Place Order")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("\n----- Place Order -----")
                print("1. Add Item to Order by Code")
                print("2. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == '1':
                    print("\n------- Menu -------")
                    with open(menu_file, newline='') as file:
                        reader = csv.DictReader(file)
                        for i, row in enumerate(reader, start=1):
                            print(f"{i}. {row['item']} - ${float(row['price']):.2f}")  # Convert price to float

                    item_code = int(input("Enter item code: "))
                    quantity = int(input("Enter quantity: "))

                    items = list(order_manager.menu.keys())
                    if 1 <= item_code <= len(items):
                        item_name = items[item_code - 1]
                        total_cost = order_manager.place_order(item_name, quantity)
                        print("Thank you for your order!")
                        print(f"Total bill amount: ${total_cost:.2f}")
                    else:
                        print("Invalid item code.")
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == '2':
            print("Exiting Order Management.")
            home.main()
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
