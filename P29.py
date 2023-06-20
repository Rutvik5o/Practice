#W.A.P take Rollercoaster Ride example again but there want to add one more thing now if you want a photo durin Ride then extra 50 Rs you need to pay no matter of what age you are.



height= int(input("what is you height? "))

bill=0

if height >=3:

    print("You can Ride")

    age=int(input("what is your age?"))

    if age < 12:

        bill=150

        print("Ticket Price is 150 Rs")

    elif age <= 18:

        bill=250

        print("Ticket Price is 250 Rs")

    else:
         bill=500

         print("Ticket Price is 500 Rs")

    want_photo=input("Do You want to take photo (Y|n)? ")

    if want_photo == 'Y' or want_photo == 'y':

        bill+=50

        print(f"Your Total bill is {bill}")

    else:

        print("You can't Ride")


print("Thank You.... Enjoy the Ride!")
