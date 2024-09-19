class student:

    dept = "IT"


    def __init__(self,r,n):

        self.roll = r

        self.name = n


obj = student(1,"abc")

print(obj.roll)
print(obj.name)

print(student.dept)