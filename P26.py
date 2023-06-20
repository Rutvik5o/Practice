# Nested if-else & elif

height=int(input("whar is your height in feet?"))

if height>= 3:
    print("You can Ride")

    age=int(input("what is your age?"))

    if age<=18:
        print("Pay 250 RS")

    else:
        print("Pay 500 RS")

else:
    print("can't Ride")


print("Using elif function ")

height=int(input("what is your height in feet?"))

if height >=3:
    print(" You can Ride")

    age=int(input("what is your age?"))

    if age<12:
        print("Pay 150 RS")

    elif age<=18:
        print("Pay 250 RS")

    else:
        print("Pay 500 RS")

else:
    print("cant' Ride")