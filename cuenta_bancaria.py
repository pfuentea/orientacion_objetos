class BankAccount:
    def __init__ (self,int_rate,balance=0):
        self.saldo=balance
        self.interes=int_rate
    def deposit(self,amount):
        self.saldo +=amount
        return self
    def withdraw(self,amount):
        self.saldo -=amount
        return self
    def display_acount_info(self):
        print (f"Esta cuenta posee: ${self.saldo} piticlines.")
        return self
    def yield_interest(self):
        if(self.saldo>0):
            self.saldo += self.saldo*self.interes
        return self

cuenta1=BankAccount(0.01,1000)
cuenta2=BankAccount(0.02,5000)

cuenta1.deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_acount_info()

cuenta2.deposit(5000).deposit(5000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_acount_info()
