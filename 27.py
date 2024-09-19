def rename(duplicate):

    final_list = []

    for x in duplicate:

        if x not in final_list:

            final_list.append(x)

        else:

            print("Number is repeating",x)


    print(final_list)


rename([34,255,22,3,5,56,6,2,1,3,5,2,3,62])