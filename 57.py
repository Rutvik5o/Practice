class Bank:

    def __init__(self,name,balance):

        self.name = name

        self.balance = balance


    def display(self,deposite,withdrawl):

        print("Name=>",self.name)

        print("Deposit=>",deposite)

        print("Balance =>",self.balance)

        print("Withdrawl=>",withdrawl)


Obj1= Bank("Hi",500)

Bank.display(Obj1,200,300)