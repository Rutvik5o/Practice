def checkprime():

    num = int(input("Enter a number you want to check prime->"))


    if num <= 1:

        print("Number is not prime")

        return 

        print("hello")


    c = 0

    for i in range(1,num + 1):

        if num % i == 0:

            c += 1


    if c == 2:

        print("Number is primee", num)

    else:

        print("Number is not prime")

checkprime()