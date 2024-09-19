#common and no common using membership operators.

list1= [1,2,343,5,25,3]

list2= [53,2,23,343,25]


c=[]
nc=[]

for x in list1:

    if x in list2:

        c.append(x)

    else:

        nc.append(x)

    
print("common=>",c)

print("non common=>",nc)