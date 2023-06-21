# Random Module


#randint(a,b) a<= x <=b

#randrange(a,b) a<= x < b [B was not include]



import random

a=random.randint(1,3)

print(a)


#a=randran(1,3) wrong syntax

a=random.randrange(1,3) # 3 not include

print(a)


a=random.random() # print between 0.0 -> 0.9 float randomly

print(a)


print("Uniform")

a=random.uniform(1,3)

print(a)



print("Choice")

l=[2,5,9,10]

a=random.choice(l)

print(a)


print("Shuffle")

Y=[5,35,25,3]

random.shuffle(Y)

print(Y)
