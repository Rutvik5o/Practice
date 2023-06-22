# Nested List

list1=[10,34,593,35,[58,359,-53],3,35]

print(len(list1))

print(list1[4][2])  # -> Invidual We cann als select with nested

print(list1[len(list1)-2])

print(list1[4][:]) # -> Print Nested list


print(list1[4][::2])  #-> skip 2 step

list2=[10,34,89,['Mohan',"Sunil","Dhrupal"],4]

print(list2[3][2])