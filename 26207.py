def rename(duplicate):

    final_list = []


    for num in duplicate:

        if num not in final_list:

            final_list.append(num)

        else:

            print(num," is repeating")

    return final_list


print("Removing duplicate number->",rename([53,53,3,35,25,21,23,3,3]))