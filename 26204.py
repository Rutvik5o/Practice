def bubblesort(list1):

    for i in range(0,len(list1)-1):

        for j in range(0,len(list1)-1):

            if list1[j] > list1[j+1]:

                temp = list1[j]

                list1[j] = list1[j+1]

                list1[j+1] = temp


    return list1

print("Sorted Array=>",bubblesort([53,66,262,12,53,23]))