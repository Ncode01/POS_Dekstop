import csv
import home

class InventoryManagement:
    def __init__(self, inventory_file):
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        inventory = {}
        try:
            with open(self.inventory_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    inventory[row['item']] = int(row['quantity'])
        except FileNotFoundError:
            # If the inventory file doesn't exist, create an empty inventory
            inventory = {}
        return inventory

    def save_inventory(self):
        with open(self.inventory_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item', 'quantity'])
            writer.writeheader()
            for item, quantity in self.inventory.items():
                writer.writerow({'item': item, 'quantity': quantity})

    def display_inventory(self):
        print("\n------- Inventory -------")
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        self.save_inventory()

    def update_quantity(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] = quantity
            self.save_inventory()
        else:
            print(f"{item} not found in inventory.")

def main():
    inventory_file = 'inventory.csv'
    inventory_manager = InventoryManagement(inventory_file)

    while True:
        print("\n----- Inventory Management -----")
        print("1. Display Inventory")
        print("2. Add Item to Inventory")
        print("3. Update Item Quantity")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory_manager.display_inventory()
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            inventory_manager.add_item(item, quantity)
            print(f"{quantity} {item}(s) added to inventory.")
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            inventory_manager.update_quantity(item, quantity)
            print(f"Quantity of {item} updated to {quantity}.")
        elif choice == '4':
            print("Returning to Main Menu.")
            home.main() 
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
