class BankAccount:
    def __init__(self, account_holder_name, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        print(f"Account created for {self.account_holder_name} with initial balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder_name}")
        print(f"Current balance: ${self.balance:.2f}")

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder_name, initial_balance=0):
        if account_holder_name in self.accounts:
            print(f"Account for {account_holder_name} already exists.")
        else:
            new_account = BankAccount(account_holder_name, initial_balance)
            self.accounts[account_holder_name] = new_account
            print(f"New account for {account_holder_name} successfully created.")

    def get_account(self, account_holder_name):
        return self.accounts.get(account_holder_name)

    def run(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Create New Account")
            print("2. Access Existing Account")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter new account holder name: ")
                initial_bal = float(input("Enter initial deposit amount: "))
                self.create_account(name, initial_bal)
            elif choice == '2':
                name = input("Enter account holder name: ")
                account = self.get_account(name)
                if account:
                    while True:
                        print(f"\n--- {account.account_holder_name}'s Account ---")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Back to Main Menu")
                        account_choice = input("Enter your choice: ")

                        if account_choice == '1':
                            amount = float(input("Enter amount to deposit: "))
                            account.deposit(amount)
                        elif account_choice == '2':
                            amount = float(input("Enter amount to withdraw: "))
                            account.withdraw(amount)
                        elif account_choice == '3':
                            account.check_balance()
                        elif account_choice == '4':
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Account not found.")
            elif choice == '3':
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()