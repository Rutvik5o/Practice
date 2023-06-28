def greet1(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department")
greet1(name="XYZ",dept="CS")  #Any position you can see that argument.


#greet(dept="CS"," XYZ") // that wrong position with parameter position

print("Keyword Argument should be after positional Argument.")

print("By Default Argument")

def greet(name,subject,dept="CS"):
    print(f"Hi {name}")
    print(f"Do you Teach {subject}")
    print(f"Are you from {dept} Department?")

greet("Anonymous","Ethical Hacking")

greet("Anonymous","Ethical Hacking","HR") # function orveride argument


print("Arbitrary Argument")

def add(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f"Sum is {c}")

add(5,9,899)

add(95,59999,9929,59)
