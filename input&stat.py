
'''
name=input("What is your name?")#=> that is input from user

print(name,"Hello")  
'''

import statistics

exlist=[34,3,6,66,4,6,7,3,44]

x=statistics.mean(exlist)

print(x)

x=statistics.median(exlist)

print(x)

x=statistics.mode(exlist)

print(x)


x=statistics.stdev(exlist)

print(x)

x=statistics.variance(exlist)

print(x)
