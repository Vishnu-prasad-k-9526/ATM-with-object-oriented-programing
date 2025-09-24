class Account:
    def __init__(self,account_number,name,balance==0.0):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("{amount} deposited successfully.")
        else:
            print("Deposite must be postive.")
    
    def Withdraw(self,amount):
        if amount>self.balance:
            print("Insufficnet balance.")
        elif amount<=0:
            print("WIthdrawal amount must be  postive.")
        else:
            self.balance-=amount
            print("{amount} withdrwan sucessfully")  

    def get_balance(self):
        return self.balance

    def display(self):
        print("AccountNumber:{self.account_number}")   
        print("AccountHolder: {self.name}")  
        print("Balance {self.balance}")

class BANK:
    def __init__(self):
        self.accounts={}
    
    def create_account(self,account_number,name,intial_deposit=0.0):
        if account_number in self.accounts:
            print("Acoount Number all Ready exist")
        else:
            account=Account(account_number,name,intial_deposit)
            self.accounts[account_number]=account
            print("account created successfully")
    
    def get_account(self,account_number):
        account=self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found")
            return None
    
    def display_all_accounts(self):
        if not self.accounts:
            print("NO acccounts in Bank.")
        else:
            for account in self.accounts.values():
                account.display()
                print("_"*20)

    def main():
        bank=BANK()
        while True:
            print("\n---Welcome to SBI bank---")
            print("1.Create account")
            print("2.Deposit MOney")
            print("3.Withdraw Money")
            print("4.Check Balance")
            print("5.Display All Accounts")
            print("6.EXist")

choice=input("Enter your choice")
if choice=='1':
    account_number=input("Entrer account number:")
    name=input("Enter holder name:")
    intial_deposit=float(input("Enter initail deposit(deafult 0):"))
    bank.create_account(account_number,name,intial_deposit)

elif choice=='2':
    account_number=input("Enter account number:")
    account=bank.get_account(account_number)
    if account:
        amount=float(input("Enter deposit amount:"))
        account.deposit(amount)
    
    elif choice=='3':
        account_number=input("Enter account number:")
        account=bank.get_account(account_number)
        if account:
            amount=float(input("Enter the withdrawal amount:"))
            account.withdraw(amount)
        
        elif choice=='4':
            account_number=input("Enter account number:")
            account=bank.get_account(account_number)
            if account:
                print("Account Balance:{account.get_balance()}")

            elif choice=='5':
                bank.display_all_account()
            
            elif choice=='6':
                print("Thank you for using SBI Bank!")
                break

            else:
                print("Invalid choice please try again.")

    


