class User:
    def __init__ (self,name,email):
        self.name = name
        self.email= email
        self.account_balance=0

    def make_deposit(self,amount):
        self.account_balance+=amount
    def make_withdrawl(self,amount):
        self.account_balance-=amount
    def display_user_balance (self):
        print(self.name+' tiene :$'+str(self.account_balance)+' en su cuenta.')
    def transfer_money (self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
pedro = User("Pedro Picapiedra", "ppicapiedra@bedrock.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
guido.display_user_balance()
monty.display_user_balance()

