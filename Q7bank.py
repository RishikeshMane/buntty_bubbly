class bank:
    def __init__(self):
        self.balance=0
        print("the account is created")
        while 1:
            choice = int(input("enter 1 to deposit & 2 to withdraw :- "))
            if(choice==1):
                self.deposit()

            else:
                self.withdrwal()

    def deposit(self):
        amount=float(input("enter the amount to deposited :- "))
        self.balance=self.balance+amount
        print("deposit is successful balance is %f"% self.balance)

    def withdrwal(self):
        amount=float(input("enter the amount to be withdrawal :- "))
        if(amount <= self.balance):
            self.balance=self.balance-amount
            print("withdrwal successful, balance is %f"%self.balance)
        else:
            print("error")
acc=bank()