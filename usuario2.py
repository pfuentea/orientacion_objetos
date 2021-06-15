from cuenta_bancaria import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self,amount):
        if self.account.saldo<amount:
            print("Saldo insuficiente")
        else:
            self.account.withdraw(amount)
        return self
    def display_user_balance (self):
        self.account.display_acount_info()
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        print(f"Se realiazó una tef desde {self.name} hacia {other_user.name} por la cantidad de :{amount}")
        return self

ani = User("Anakin Skywalker", "vader@sith.com")
pedro = User("Din Djarin", "mando@mandalor.com")
ani.make_deposit(321) 
ani.make_withdrawl(121)
ani.display_user_balance() 

pedro.make_deposit(1000).make_withdrawl(100).make_withdrawl(154).make_withdrawl(238).display_user_balance()

ani.transfer_money(pedro,150) 