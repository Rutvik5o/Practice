'''
(4) => Write a program to store data into instancdes using mutator method and to retrieve data from instances using accessor method.
'''

class student:

    def __init__(self):

        self.name = "Xyz"


    def getter(self):

        return self.name


    def setter(self):

        self.name = "ABC"


Obj = student();

print("Before setter method=>",Obj.getter())

Obj.setter();

print("After setter method=>",Obj.getter())

   


