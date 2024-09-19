## override super class constuctor


class a:

    def __init__(self):

        self.name = "abc"


    def display(self):

        print(self.name)


class b(a):

    def __init__(self):

        super().__init__()

        self.name = "xyz"

    def display(self):

        print(self.name)


obj = b()
obj.display()