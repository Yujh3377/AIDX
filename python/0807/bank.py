class BankAccount:
    def __init__(self,balance=100000):
        self.name ="Hong"
        self.__balance=balance
    def whithdraw(self, amount):
        self.__balance -= amount
        print("통장에서 ",amount,"가 출금되었습니다.")
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
        print("통장에서 ",amount,"가 입금되었습니다.")
        return self.__balance
    
cus1 =BankAccount()
cus1.deposit(100)
cus1.whithdraw(10)