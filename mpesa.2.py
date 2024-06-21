class Account:
    def __init__(self,Account_holder,balance):
        self.Account_holder= Account_holder
        self.balance= balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"You have successfully deposited {amount} to your account at 12:32 am. New M-pesa balance is {self.balance}")
        else:
            print("The amount should be more than 0")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount}. Your new balance is {self.balance}")
    def __str__(self):
        return f"{self.Account_holder}\nBalance{self.balance}"

class Savingsaccount(Account):
    def __init__(self,Account_holder,balance,interest_rate):
        super().__init__(Account_holder,balance)
        self.interest_rate= interest_rate
account= Account('Kiplangat',12300)
account.deposit(1200)
account.withdraw(2000)
print()
savings= Savingsaccount('Vincent kiplangat',1200)
Savingsaccount.deposit(2300)
(12)
