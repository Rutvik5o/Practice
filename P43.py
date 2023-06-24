# for else in python

tuple1=(2,57,5,34,3,-1)


for i in tuple1:
    print(i)

    if i==5:
        break


else: # whole loop terminate when its get 5
    print("Loop Completed & WE are in else block Now.")

print("Out of For/else")


tuple1=(5,57,34,5,-1)

for i in tuple1:

    if i%6==0:
        print(i)
        break

    #else:
        print("There is no number Divide by 6.")

else:
    print("There is no number Divide by 6")