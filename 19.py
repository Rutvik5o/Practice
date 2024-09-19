#Write a program in seach an element in the list using for loop and also demostrate the use of "else" with for loop.

list1= [3,5,63,4,23,6,1]


num = int(input("Enter the number you want to search->"))

for x in list1:

    if x == num:

        print("Given Element Exist")

        break

        

else:

    print("elements not exist")



