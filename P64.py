#Excercise 12
#-> Prime Number


import math

def prime_checker(number):
    is_prime=True
    if number == 1:
        is_prime=False

    for i in range (2,math.ceil(number/2)+1):
        if number% i ==0:
            is_prime=False

    if is_prime==True:
            print("It is a Prime Number.")

    else:
            print("This Number is not prime number.")


n=int(input("Enter a Number:\n"))

prime_checker(n)