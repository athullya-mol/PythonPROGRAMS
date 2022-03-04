class bank_account():
    def __init__(self):
        self.accno="4597126"
        self.name="madhav"
        self.typeofacc="SB"
        self.balance=15000
    def print(self):
        print(self.accno)
        print(self.name)
        print(self.typeofacc)
        print(self.balance)
    def deposit(self):
        amount=int(input("Enter amount to be deposited"))
        self.balance=self.balance+amount
        print("\n Amount Deposited",amount)
        print("\n Available balance is:",self.balance)

    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
        if self.balance>=amount:
             self.balance-=amount
             print("you withdrew:",amount)
        else:
            print("\n insufficient balance")
    def display(self):
        print("\n Net available balance=",self.balance)
print("Hello, Customer!")
s=bank_account()
print("Your details are...")
s.print()
s.deposit()
s.withdraw()
s.display()
            
                   
