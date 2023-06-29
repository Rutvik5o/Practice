import random
#args and **kwargs

def add(*numbers,name):  #-> consider as tuple
    c=0
    print(numbers)
    print(name)

    for i in numbers:
        c+=i
    print(f"Sum is {c}")

add(1,2,4554,name="XYZ")

print("*args")

def add(a,*numbers):
    c=0
    print(a)
    print(numbers)
    for i in numbers:  #-> a consider as first argument
        c+=i
    print(f"Sum is {c}")

add(1,2,5,7)

print("**kwargs") #-> Default->APosition->AKeyword

def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

info_person(name="Ram",age=30,dept="CSE")
info_person(name="Shyam",dept="HR")

print("One More Example")

def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)

info_person(1,3,name="Ram",age=30,dept="CSE")
info_person(45,78,name="Shyam",dept="HR")


