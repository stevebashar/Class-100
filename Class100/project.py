class Bankatm():
    def __init__(self, deposit, withdraw, balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.balance = balance

    def depositmoney(self, deposit):
        print("You have deposited $150")

    def withdrawmoney(self):
        print("You have withdrawed $200")

    def checkBalance(self):
        print("Your balance is $1250")

atm = Bankatm("$150", "$200", "$1250")
print(atm.withdraw)
print(atm.balance)
print(atm.deposit)