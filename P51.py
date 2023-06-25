print("Break")

list1=['hi','hello','welcome']

names=['Krishna','Ram','Madhav']

for item in list1:
    for name in names:
        print(item,name)
        if item == 'hello' and names=='Ram':
            break
    print("Out Form Inner Loop")

print("Out from outer loop")


print("Continue")

for i in range(1,11):
    if i == 7:
        continue
    else:
        print(i)

print("Pass")

for i in range(1,11):
   pass





