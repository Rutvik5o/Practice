#Nestng dictonary & list

student_data={
       "Ram":{"roll_no":10,"age":20,"course":"Python"},
       "Mohan":{"roll_no":20,"age":22,"course":"Java"}
}

print(student_data["Mohan"])
print(student_data["Ram"]["course"])

student_data["Mohan"]["phone_no"]=9593959363

print(student_data["Mohan"])


#del student_data["Mohan"]["phone_no"] #-> delete list in dictonary in key

#print(student_data["Mohan"])


#-> using pop (Return Deleted value)

print(student_data["Mohan"].pop("phone_no"))

print(student_data["Mohan"])

#-> Nesting list within Dictnory

travel_data={

    "Gujarat":["Dwarka","Somnath","Statue of Unity"],
    "Rajashtan":["Jaipur","Udhaipur"]

}

print(travel_data["Rajashtan"])

#-> One more example also enter dictnory new key

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
    "Age":32,n
    "Course":"Java",
    "Phone_No":[38593935,3953975]
   }
]

print(student_data[1]["Phone_No"])