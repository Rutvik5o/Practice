def checkrprime():

    num = int(input("Enter the number->"))


    if num <= 1:

        print("Enter valid number")


    c = 0


    for i in range(1,num+1):

        if num % i == 0:

            c += 1



    if c == 2:

        print("Number is prime")

    else:

        print("Number is not prime")

checkrprime()