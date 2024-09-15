list1=[35,3,23,55,622,12]

n=0

n=int(input("Enter number you want to search->"))

for x in list1:

    if x == n:

        print("Element found=>", n)

        break

else:
    print("Element not found")

