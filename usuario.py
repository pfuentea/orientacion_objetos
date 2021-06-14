class User:
    def __init__ (self,name,email):
        self.name = name
        self.email= email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance+=amount
        return self
    def make_withdrawl(self,amount):
        if self.account_balance<amount:
            print("Saldo insuficiente")
        else:
            self.account_balance-=amount
        return self
    def display_user_balance (self):
        print(self.name+' tiene : $'+str(self.account_balance)+' en su cuenta.')
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self

ani = User("Anakin Skywalker", "vader@sith.com")
padme = User("Padmé Amidala", "pamidala@senate_Stellar.com")
pedro = User("Din Djarin", "mando@mandalor.com")

'''
ani.make_deposit(100)
ani.make_deposit(200)
ani.make_deposit(321)
ani.make_withdrawl(121)
ani.display_user_balance()
'''

ani.make_deposit(100).make_deposit(200).make_deposit(321).make_withdrawl(121).display_user_balance()

'''
padme.make_deposit(50)
padme.make_deposit(500)
padme.make_withdrawl(60)
padme.display_user_balance()
'''
padme.make_deposit(50).make_deposit(500).make_withdrawl(60).display_user_balance()

'''pedro.make_deposit(1000)
pedro.make_withdrawl(100)
pedro.make_withdrawl(154)
pedro.make_withdrawl(238)
pedro.display_user_balance()
'''
pedro.make_deposit(1000).make_withdrawl(100).make_withdrawl(154).make_withdrawl(238).display_user_balance()

ani.transfer_money(pedro,150)

ani.display_user_balance()
pedro.display_user_balance()

#import pdb; pdb.set_trace()

