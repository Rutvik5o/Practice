class student:

    def __init__(self,name,age,no):

        self.name = name

        self.age = age

        self.no = no


    def display(self):

        print(self.name,self.age,self.no)


s1=student("Hi",14,74)

s1.display()