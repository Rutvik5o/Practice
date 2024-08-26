arr1=[53,56,3,366,72]

arr2= [None] * len(arr1)


for i in range(0,len(arr1)):

    arr2[i] = arr1[i]


print("Printing Original Array->")

for i in range(0,len(arr1)):
    print(arr1[i])

for i in range(0,len(arr1)):
    print(arr2[i])


