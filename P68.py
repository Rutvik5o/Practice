#Excercise 68
student_marks={
  "XYZ":92,
  "Harry":88,
  "Dimpy":76,
  "Rahul":63,
  "Aniket":56,
  "Hiok":43,
  "Prem":34
  }

student_grades={}


for student in student_marks:
    marks=student_marks[student]
    if marks >= 90:
        student_grades[student]= "A+"
    elif marks > 80:
        student_grades[student]= "A"
    elif marks > 70:
        student_grades[student]= "B+"
    elif marks > 60:
        student_grades[student]= "B"
    elif marks > 50:
        student_grades[student]= "C"
    elif marks > 40:
        student_grades[student]= "D"
    else:
        student_grades[student]="F"


print(student_grades)



