import sys

n=int(sys.argv[1])
i=2
sum=0

while(i<=n):
    sum += i
    i += 2

print("Sum",sum)