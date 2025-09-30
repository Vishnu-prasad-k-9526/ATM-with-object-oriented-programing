class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number   
        self.__holder_name = holder_name         
        self.__balance = balance                 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")
    
    def get_balance(self):
        return self.__balance
    
    def show_details(self):
        print(f"Account No: {self.__account_number}, Holder: {self.__holder_name}, Balance: ₹{self.__balance}")

class ATM(Account):
    def __init__(self, account_number, holder_name, balance=0, pin="0000"):
        super().__init__(account_number, holder_name, balance)  
        self.__pin = pin
    
    def validate_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    def show_details(self):
        print(f"ATM Account [{self.get_account_number()}] - Holder: {self.get_holder_name()} - Balance: ₹{self.get_balance()}")
    
    def get_account_number(self):
        return self._Account__account_number
    def get_holder_name(self):
        return self._Account__holder_name
    def get_balance(self):
        return self._Account__balance

atm_user = ATM("123456789", "Alice", 5000, "1234")
print("=== Welcome to the ATM ===")
pin = input("Enter your PIN: ")
if atm_user.validate_pin(pin):
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account Details")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Your balance is: ₹{atm_user.get_balance()}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm_user.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm_user.withdraw(amount)
        elif choice == "4":
            atm_user.show_details()
        elif choice == "5":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN! Access denied.")