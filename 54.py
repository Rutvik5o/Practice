class fun:


    def __init__(self):

        self.name = "abc"


    def getter(self):

        return self.name

    def setter(self):

        self.name = "xyz"


obj = fun()
print(obj.getter())

obj.setter()

print(obj.getter())




