#print("While Loop")

count=1

while count<=5:
    print(count)
    count += 1

else:
    print("\n Else Block")#->else part also execute

print("Out Form Loop")

print("2nd Example")

count=10

while count>0: print(count); count-=1 #->short
print("Out From Loop")

while True:
    print(count)
    count += 1;
    if count ==5: #-> here loop terminated
        break
else:
    print("\n In else block")

print("Out from loop")





print("Using Break other example")

count=1

while count<=5:
    print(count)
    count += 1

    if count == 3:
        break  #-> here break terminate program there other statement of loop not execute.

else:
    print("\n Else Block")#->else part also execute

print("Out Form Loop")

print("A New Example")

total=0

Number=int(input("Enter a Number(0 to quit)"))

while Number!=0:
    total=total+Number
    Number=int(input("Enter a Number(0 to quite:"))

print("Total is:",total)