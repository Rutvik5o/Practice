arr1= [1,2,34,5]

arr2= [None] * len(arr1)

for i in range(0,len(arr2)):

    arr2[i] = arr1[i]

print(arr2)