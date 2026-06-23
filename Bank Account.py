class BankAccount:
    def __init__(self,name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self._balance=balance
    def Deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")
    def Withdraw(self,amount):
        if amount<=0:
            print("Invalid withdrawal amount!")
        elif amount>self._balance:
            print("Insufficient balance!")
        else:
            amount<self._balance
            self._balance-=amount
            print(f"Rs.{amount} withdrawn successfully.")
    def Show_balance(self):
        print(f"Current balance:Rs.{self._balance}")
    def Show_details(self):
        print("\n---Account Details---")
        print(f"Account holder: {self.name}")
        print(f"Account number: {self.account_number}")

account1=BankAccount("Zainab","ACC001",5000)
account1.Show_details()
print()
account1.Show_balance()
account1.Deposit(10000)
account1.Show_balance()
account1.Withdraw(5000)
account1.Show_balance() 

account2=BankAccount("Noor","ACC002",2000)      
account2.Show_details()
print()
account2.Show_balance()
account2.Deposit(5000)
account2.Show_balance()
account2.Withdraw(2500)
account2.Show_balance() 