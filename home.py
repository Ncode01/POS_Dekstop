import order_management
import inventory_management 

def main():
    print("Welcome to the Home Page!")
    
    while True:
        print("\n----- Main Menu -----")
        print("1. inventry Management")
        print("2. Menu Management")
        print("3. Place Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            
            pass

        elif choice == '2':
          inventory_management.main()
            

        elif choice == '3':
            order_management.main()

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
