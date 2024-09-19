

class parent:

    def __init__(self):

        print("to program")
        self.a=10


    def display(self):

        print("hello bro")

    


class child(parent):

    a=50

    def __init__(self):

        print("welcome")

        super().__init__()

       

    def display(self):

        print("going to parent class")

        super().display()

        print(self.a)
        

    

c=child()
c.display()