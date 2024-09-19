class test:


    def __init__(self,name,balance):

        self.name = name

        self.balance = balance


    def display(self,withdraw,deposit):

        print("Name=>",self.name)

        print("Balance =>",self.balance)

        print("withdraw=>",withdraw)

        print("Deposit=>",deposit)


obj = test("abc",1000)

obj.display(100,200)

