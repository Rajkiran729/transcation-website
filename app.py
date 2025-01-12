import os

class TransactionApp:
    def __init__(self):
        self.users = {}

    def create_user(self, username, initial_balance=0):
        if username in self.users:
            print(f"User '{username}' already exists.")
            return False
        self.users[username] = initial_balance
        print(f"User '{username}' created with balance {initial_balance}.")
        return True

    def deposit(self, username, amount):
        if username not in self.users:
            print(f"User '{username}' does not exist.")
            return False
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False
        self.users[username] += amount
        print(f"Deposited {amount} to '{username}'. New balance: {self.users[username]}.")
        return True

    def withdraw(self, username, amount):
        if username not in self.users:
            print(f"User '{username}' does not exist.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        if self.users[username] < amount:
            print("Insufficient balance.")
            return False
        self.users[username] -= amount
        print(f"Withdrew {amount} from '{username}'. New balance: {self.users[username]}.")
        return True

    def transfer(self, from_user, to_user, amount):
        if from_user not in self.users or to_user not in self.users:
            print("One or both users do not exist.")
            return False
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return False
        if self.users[from_user] < amount:
            print("Insufficient balance for transfer.")
            return False
        self.users[from_user] -= amount
        self.users[to_user] += amount
        print(f"Transferred {amount} from '{from_user}' to '{to_user}'.")
        return True

    def check_balance(self, username):
        if username not in self.users:
            print(f"User '{username}' does not exist.")
            return None
        print(f"Balance for '{username}': {self.users[username]}.")
        return self.users[username]

    def display_users(self):
        if not self.users:
            print("No users found.")
            return
        print("Users and balances:")
        for username, balance in self.users.items():
            print(f"{username}: {balance}")

if __name__ == "__main__":
    app = TransactionApp()

    while True:
        print("\nTransaction App")
        print("1. Create User")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Display All Users")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            initial_balance = float(input("Enter initial balance (default 0): ") or 0)
            app.create_user(username, initial_balance)

        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter deposit amount: "))
            app.deposit(username, amount)

        elif choice == "3":
            username = input("Enter username: ")
            amount = float(input("Enter withdrawal amount: "))
            app.withdraw(username, amount)

        elif choice == "4":
            from_user = input("Enter sender's username: ")
            to_user = input("Enter receiver's username: ")
            amount = float(input("Enter transfer amount: "))
            app.transfer(from_user, to_user, amount)

        elif choice == "5":
            username = input("Enter username: ")
            app.check_balance(username)

        elif choice == "6":
            app.display_users()

        elif choice == "7":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
