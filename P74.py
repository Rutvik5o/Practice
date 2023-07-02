print("MultiReturn Statement")

import statistics

def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    print("This will not print")

a,b,c=mean_median_mode([3,5,45,3,2,1,89])
print(f"Mean is {a}\nMedian is {b}\nmode is {c}")

print("This is example of single statement return multiple value")






print("One More Example")

def add(a,b):
    if a==0 & b==0:
        return #we can print anything here

    else:
        return a+b


var1=int(input("Enter First Variable"))
var2=int(input("Enter Second Variable"))

result=add(var1,var2)
print(result)

print("We see here multiple return statement within single function")

print("single Return statement multiple value")