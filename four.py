list1= [1,2,35,52,35,6,3,21,23]

list2= [63,32,2,53,2,452,52,1]

c=[]

nc=[]

for x in list1:

    if x in list2:

        c.append(x)
    else:

        nc.append(x)

else:

    print("Process completed sucessfully")


print("common->",c)
print("non common->",nc)