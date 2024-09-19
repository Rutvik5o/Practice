#create a python function to accpect python function as a dictionary and display its elemnts.


def func(dict1):

    for x in dict1:

        print("Key->",x)

        print("Value->",dict1[x])


func({1:'abc',2:'cac',3:'yyy'})