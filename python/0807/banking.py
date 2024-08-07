class BankAccount:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name,number,balance)
        self.withdraw_change=10000
        
    def withdraw(self, amount):
        return super().withdraw(self,amount+self.withdraw)
class SavingAccount(BankAccount):
    def __init__(self,name ,number, balance):
        super().__init__(name,number,balance)
        self.interest_rate=0.03
    def add_interest(self):
        return super().withdraw(self,self.balance+self.withdraw)
    
a1=SavingAccount("홍길동",123456,10000,0.05)
a1.add_interest()
print("저축예금의 잔액=",a1.balance)

a2=CheckingAccount("김철수",123457,2000000)
a2.withdraw(10000)
print("당좌예금의 잔액=",a2.balance)

