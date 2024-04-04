import home

class LoginSystem:
    def __init__(self):
        self.credentials = {'1': '1', 'user2': 'password2'}  # Sample credentials, replace with your own

    def login(self, username, password):
        if username in self.credentials and self.credentials[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False


def main():
    login_system = LoginSystem()

    while True:
        print("\n----- Login -----")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if login_system.login(username, password):
            home.main()  # Call the main function of home.py
            break


if __name__ == "__main__":
    main()
