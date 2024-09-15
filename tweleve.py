len = int(input("Enter length in centimeter->"))

if len < 0:

    print("invalid input")

else:

    inch = len/2.54

    print(len, "centimeter is equal to ->", inch, "inches")