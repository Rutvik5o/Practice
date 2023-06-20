# W.A.P. to check whether given year is leap year or not.


year=int(input("Which year year you want to check? "))

if year % 4==0:

    if year % 100 ==0:

        if year % 400 ==0:

             print("Leap Year")

        else:

            print("Not Leap Year")

    else:

        print("Leap Year")

else:

    print("Not Leap Year")