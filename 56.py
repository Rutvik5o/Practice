class temp:

    count = 0

    def __init__(self):

        temp.count += 1 

    @staticmethod

    def display():

        print("Total Object Created=>",temp.count)
    
Obj = temp()
Obj2=temp()
Obj2.display()