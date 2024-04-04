import csv
import home

class MenuManagement:
    def __init__(self, menu_file):
        self.menu_file = menu_file
        self.menu = self.load_menu()

    def load_menu(self):
        menu = {}
        if self.menu_file and self.menu_file.strip() != "":
            try:
                with open(self.menu_file, newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        menu[row['item']] = float(row['price'])
            except FileNotFoundError:
                print("Menu file not found.")
        return menu

    def add_item(self, item_name, price):
        self.menu[item_name] = price
        self.save_menu_to_file()

    def edit_item(self, item_name, new_price):
        if item_name in self.menu:
            self.menu[item_name] = new_price
            self.save_menu_to_file()
            print(f"{item_name} price updated to ${new_price:.2f}")
        else:
            print("Item not found in the menu.")

    def display_menu(self):
        print("\n------- Menu -------")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def save_menu_to_file(self):
        with open(self.menu_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item', 'price'])
            writer.writeheader()
            for item, price in self.menu.items():
                writer.writerow({'item': item, 'price': price})


def main():
    menu_file = 'menu.csv'
    menu_manager = MenuManagement(menu_file)

    while True:
        print("\n----- Menu Management -----")
        print("1. Add Item")
        print("2. Edit Item Price")
        print("3. Display Menu")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            price = float(input("Enter price: "))
            menu_manager.add_item(item_name, price)

        elif choice == '2':
            item_name = input("Enter item name to edit: ")
            new_price = float(input("Enter new price: "))
            menu_manager.edit_item(item_name, new_price)

        elif choice == '3':
            menu_manager.display_menu()

        elif choice == '4':
            print("Exiting Menu Management.")
            home.main()
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
