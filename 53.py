class student:

    field = "IT"

    def __init__(self,r,n):

        self.roll = r

        self.name = n



Obj = student(10,"ABC")

print(student.field,Obj.roll,Obj.name,Obj.field)