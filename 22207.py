def rename(duplicate):

    final_list = []


    for x in duplicate:

        if x not in final_list:

            final_list.append(x)

        else:

            print(x," number is repeating")


    return final_list

print("Removing duplicate elemetns=>",rename([543,53,53,3,3,3,33,525,32,87]))