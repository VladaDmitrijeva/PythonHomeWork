class BankAccount:
    def __init__(self,account_number:int,balance:int,owner_name:str) -> None:
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
    # def deposite(self, deposite:int):
    #     self.balance = self.balance + deposite

    # def withdraw(self, withdraw:int):
    #     self.balance = self.balance - withdraw
    def total(self, deposite, withdraw):
        self.balance = self.balance - withdraw + deposite 

myAcc = BankAccount(23455432, 100, "Miks Mikus")
myAcc.deposite = 20
myAcc.withdraw = 40

print(f'Current bank balance is {myAcc.total()} EUR')