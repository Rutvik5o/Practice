class ct:

    counter = 0
    
    def __init__(self):
        
        ct.counter += 1
        
        
    @staticmethod

    def display():

        print("Total Object Created=>",ct.counter)



obj1 = ct()
obj2 = ct()
obj3 = ct()

obj3.display()