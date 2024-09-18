'''
(11)=> Write a program to override super class constructor and method in sub classes.
'''


class parent:

    def __init__(self):

        self.name = "abc"


    def display(self):

        self.name = "abc"
        

        print(self.name)


class child(parent):

    def __init__(self):

        super().display() 
        super().__init__(name)


        super().__init__()

        print("Value has been changed")

    
        self.name = "xyz"

    def display(self):

        print(self.name)


Obj1= parent()
Obj1.display()

Obj2 = child()
Obj2.display()

