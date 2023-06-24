#W.A.P. t find maximum Number from a list of nUmbers

Number=input("Enter list of Numbers:")

Numbers_list=Number.split()

count=0


for Number in Numbers_list:
    count +=1

print(f"The length of the list is:{count}")

for i in range(count):
    Numbers_list[i]=int(Numbers_list[i])

maximum_Number=Numbers_list[0]

for Number in Numbers_list:
    if Number > maximum_Number:
        maximum_Number=Number


print(f"The Maximum Number is:{maximum_Number}")