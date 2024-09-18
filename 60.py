'''
(10)=> Write a program to access the base class contructor from
by using super() method and also without using super() method.
'''


class parent:

    def __init__(self):

        print("to program")


class child(parent):

    def __init__(self):

        print("Welcome")

        super().__init__()


Obj=child()



