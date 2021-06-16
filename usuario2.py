from cuenta_bancaria import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuentas=[]
        self.cuentas.append(BankAccount(int_rate=0.02, balance=0))
        #self.account = 
    def new_account(self,int_rate=0, amount=0):
        self.cuentas.append(BankAccount(int_rate, amount))
    def make_deposit(self,amount,n_cuenta=1):
        if n_cuenta <= len(self.cuentas):
            self.cuentas[n_cuenta-1].deposit(amount)
        else:
            print("Esta cuenta no existe")
        return self
    def make_withdrawl(self,amount,n_cuenta=1):
        if n_cuenta <= len(self.cuentas):
            if self.cuentas[n_cuenta-1].saldo<amount:
                print("Saldo insuficiente")
            else:
                self.cuentas[n_cuenta-1].withdraw(amount)
        else:
            print("Esta cuenta no existe")
        return self
    def display_user_balance (self):
        
        for cuenta in range(len(self.cuentas)):
            print(f"Cuenta {cuenta+1}:")
            self.cuentas[cuenta].display_acount_info()
        return self
    def transfer_money(self, other_user, amount,c1_self=1,c2_other=1):
        self.make_withdrawl(amount,c1_self)
        other_user.make_deposit(amount,c2_other)
        print(f"Se realiazó una tef desde {self.name}:cuenta {c1_self} hacia {other_user.name}:cuenta {c2_other} por la cantidad de :{amount}")
        return self

ani = User("Anakin Skywalker", "vader@sith.com")
pedro = User("Din Djarin", "mando@mandalor.com")
ani.make_deposit(321,1) 
ani.make_withdrawl(121,1)
ani.display_user_balance()
print("\nCreamos una nueva cuenta y la desplegamos") 
ani.new_account(0.1,1000)
ani.display_user_balance() 
print("\nDepositamos a Din 2 lukas") 
pedro.make_deposit(2000)
pedro.display_user_balance()
print("\nRealizamos una transferencia")
ani.transfer_money(pedro,150,2,1)  
print("\nLuego de la transferencia balance de Din")
pedro.display_user_balance()
print("\nLuego de la transferencia balance de Ani")
ani.display_user_balance() 
#pedro.make_deposit(1000).make_withdrawl(100).make_withdrawl(154).make_withdrawl(238).display_user_balance()

#ani.transfer_money(pedro,150)  