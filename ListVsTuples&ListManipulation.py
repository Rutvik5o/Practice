def example():
    return 15,19


a,b=example()

print(a)
print(b)



x=[6,4,5,44,66,33,2,55,4,4]

print(x)
print(x[5])

x.append(15)

print(x)

x.insert(4,9)  #=> enter data its specific position after 4 position 9 values added

print(x)

x.remove(9)

print(x)

print(x.index(33)) #=> for know specific data index

print(x.count(4)) #=> for know how many time values repeating

x.sort()

print(x)


y=['spot','cam','jan','dave','acod','zack']

y.sort()  #=> sort according abcd

print(y)

y.reverse()

print(y)