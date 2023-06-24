#W.A.P to calculate sum of even Numbers from 0 to 100, including i & 100.


total=0

for i in range(2,101,2):
    total += i

print(total)
#2nd Method
total=0

for i in range(1,101):
    if i%2==0:
        total += i

print(total)