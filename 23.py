from array import *

a = array('f',[234,33,22,213])

for x in range(0,len(a)):

    print(a[x])


a.insert(2,132)
print(a)

a.pop(3)
print(a)

a.remove(234)
print(a)

print(a.index(33))