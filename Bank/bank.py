class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposite(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Not enough Money in Account')

    def statement(self):
        print('Account Balance {}rs.'.format(self.balance))



class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 1000)

    def __str__(self):
        return "{}'s Current Account balance is {}".format(self.name, self.balance) 


class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Saving Account balance is {}".format(self.name, self.balance) 

user = Current('Vivek', 1000)
user.withdraw(1000)
print(user)


user2 = Saving('Test', 500)
user2.withdraw(100)
user2.deposite(500)
user2.statement()