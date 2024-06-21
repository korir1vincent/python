class Account:
    def __init__(self,Account_holder,balance,):
        self.Account_holder = Account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount>0:
            self.balance+= amount
            print(f"{amount} deposited succesfully. New balance is {self.balance}")
        else:
            print("Amount should be greater than zero")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insuffficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn succesfully.New balance is {self.balance}")
    def __str__(self):
        return f"Account holder: {self.Account_holder}\nBalance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self,Account_holder,balance,interest_rate):
        super().__init__(Account_holder,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance += interest
        print(f"Interest added successfully. New balance is {self.balance}")
    def __str__(self):
        return (f"Savings account holder: "
                f"{self.Account_holder}\nBalance: {self.balance},"
                f"interest rate: {self.interest_rate}")
    #object
account=Account(f"Vincent kiplangat", 12132)
account.deposit(100)
account.withdraw(600)
print(account)
Savings=SavingsAccount('Jeff',12300,12)
Savings.deposit(2000)
Savings.withdraw(1300)
Savings.add_interest()
print(Savings)




