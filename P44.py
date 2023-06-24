#Exercise 14

#W.A.P. to calculate average height from a list of heights

height=input("Enter all height separated by a space:")

height_list=height.split()

count=0

for height in height_list:
    count=count+1


print(count)

for i in range(count):
    height_list[i]=int(height_list[i])

total=0

for person in height_list:
    total += person

avg=total/count

print("Average height is:",round(avg))