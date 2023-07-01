#Excercise 24


student_data=[
   {
    "Name":"XYZ",
    "RollNo":11,
    "Age":22,
    "Course":"Python"
   },
   {
    "Name":"LMO",
    "RollNo":15,
    "Age":32,
    "Course":"Java",
   }
]
#-> Adding list on a memory on New Dictnory

def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student["Name"]=name
    new_student["RollNo"]=rollno
    new_student["Age"]=age
    new_student["Course"]=course_opted
    student_data.append(new_student)


add_new_student("Hexia",35,28,"C++")
print(student_data)
