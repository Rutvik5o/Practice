#Exercise 9

#Python Pizza

size=input("What size Pizza You want (S|M|L)?")

bill=0

if size == 'S' or size == 's':

    bill+=100
    print("Small Pizza Price is 100 Rs.")


elif size == 'M' or size == 'm':

    bill+=200
    print("Medium Pizza Price is 200 Rs.")


else:

    bill+=300
    print("Large Pizza Price is 300 Rs.")


add_pepperoni=input("Do you want Pepperoni (Y|N)?")


if add_pepperoni == 'Y' or add_pepperoni == 'y':

    print("Price: \n Small Pizza:30 Rs \n Medium & Large Pizza:50 Rs ")

    if size == 'S' or size == 's':

         bill+=30

    else:

        bill+=50


extra_cheese=input("Do you want extra cheese(Y|N)?")


if extra_cheese == 'Y' or extra_cheese == 'y':

     print("Price For Extra Cheese Is 20 Rs")

     bill+=20

     print(f"Your Final Bill is {bill}")





