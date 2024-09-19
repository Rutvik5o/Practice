##Write a program to find the sum of even number using commnad line argument


import sys

n=int(sys.argv[1])

i=1
sum=0

while(i<=n):

    sum += i
    i += 2

print("Sum=>",sum)