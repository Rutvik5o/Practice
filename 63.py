class a:

    def fun1(self):

        print("class a")

class b():

    def fun2(self):

        print("class b")


class c(a,b):

    def fun3(self):

        print("class c")


obj = c()
obj.fun1()
obj.fun3()