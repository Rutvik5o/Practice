# Python List


number=[10,0,2,5,-9]


names=['Jenny','Python',"C++"]


mix_list=[1,'jenny',True,1010]


print(number[1])

print(number[0:4])

print(number[0:])  # same output [Display full list]

print(number[:])  # same output [Display full list]


# Just like List synterx: print('xyz'[index:length])


Numbers=[10,2,53,-59,35]


print(Numbers[0:5:3])  # thire syntax kep the step(start from 1)

print(Numbers[0::3])


print("For Sorting List")


Numbers.sort()


print(Numbers)


print("Reverse of the list")

Numbers.reverse()

print(Numbers)


print("Min Max ")

print(min(Numbers))

print(max(Numbers))


print("Append")

Numbers.append(78)

print(Numbers)


print("Insert at Specific Position")

Numbers.insert(2,83)  #[Index,value]

print(Numbers)


print("Extend:Add Multiple value last of the list")

Numbers.extend([89,-48,35,25])

print(Numbers)


print("For Replace Index Value")

Numbers[1]=99

print(Numbers)



print("For Multi Value Replace")

Numbers[1:4]=[78,79,77]  #[Index,value]

print(Numbers)


print("For Remove specifc value")

Numbers.remove(2) # direct enter value

print(Numbers)


print("Pop: By default it's Remove last of the value & It's also Return")

Numbers.pop()

print(Numbers)

print("Pop:with Return")

print(Numbers.pop())

print(Numbers)



print("By Specific Position Remove")

print(Numbers.pop(3)) #direct enter index of the list

print(Numbers)



