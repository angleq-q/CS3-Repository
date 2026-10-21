class BankAccount:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.balance = initial_balance 
        initial_balance = 0

    def deposit(self, amount):
        if amount> 0:
            self.balance += amount
        else:
            print("ERROR")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawls must be positive")
        elif amount > self.balance:
            print("Insufficient amount.")
        else:
            self.balance -= amount
    def get_balance(self):
       return self.balance

account= BankAccount("Ana",1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())