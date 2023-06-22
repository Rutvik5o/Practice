#Excercise 12
# Split

text="Welcome to our Programming lecture"

text_splitted=text.split(" ")

print(text_splitted)


print("W.A.P. which will select a Random name from a list of names & the person selected will have to pay for everybody's food bill.")

import random

names=input("Enter Everybody's name separated by comma:")

names_list=names.split(",")

print(names_list)

length=len(names_list)

random_choice=random.randint(0,length-1)

print(f"{names_list[random_choice]} will Pay the bil.")


print("With Using Choice Function")

names=input("Enter Everybody's name separated by comma:")

names_list=names.split(",")

Person_Selected=random.choice(names_list)

print(f"{Person_Selected} will pay the bill.")


