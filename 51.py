

class student:

    def __init__(self,name,number,age):

        self.name = name

        self.number = number

        self.age = age


    def display(self):

        print("Name->",self.name)

        print("Number->",self.number)

        print("Age->",self.age)




obj= student("abc",4,21)

obj.display()
