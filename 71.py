a = int(input("Enter first Number->"))

b = int(input("Enter second number->"))

try:

    c= a/b

    print(c)

except ZeroDivisionError as e:

    print(e)

else:

    print("program completed sucessfullY")