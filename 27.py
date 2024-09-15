def rename(duplicate):

    final_list=[]


    for num in duplicate:

        if num not in final_list:

            final_list.append(num)


        else:

            print(num," is a repeating number")

        
    return final_list


print("Removing Duplicate Number=>",rename([53,52,66,26,3,3,62,11,21,11]))