# Tuple


tuple1=(12,8,"Hey",True)


print(tuple1[2])

print(type(tuple1))

print(tuple1[1:])

tuple2=(45)

print(type(tuple2))

# -> For Recognize tuple (,) shold be included

tuple3=(45,)

print(type(tuple3))

print(tuple1[::2])  #-> Skip the 2 Step of the tuple.


print(len(tuple1))


print("Nested Tuple")

tuple4=(12,5,6,True)

tuple5=(35,"Hey",'xyz')

tuple6=(tuple4,tuple5)  #-> Combine both the tuples with different Brackets.

print(tuple6)

print(tuple6[1]) #-> Print tuple 5

print(len(tuple6))

tuple6=tuple4+tuple5

print(tuple6) #-> Combine the tuples in one brackets of both tuple values.

print("Min,Max")

tuple7=(49,359,359,-3559,359,-2)

print(min(tuple7))

print(max(tuple7))

print("Count")

print(tuple7.count(359)) #-> count the specifc value number,

print("List to tuple")

list=[35,5,36]

print(tuple(list))

tuple9=(55,)*5

print(tuple9)

