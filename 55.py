class abc:
    
    dept="BCA"

    def __init__(self,name,age):

        self.name = name

        self.age = age


    def display(self):

        print("Name=>",self.name)

        print("Age=>",self.age)


Obj = abc("abc",43)
Obj.display()

Obj2=abc("xyz",53)
Obj2.display()