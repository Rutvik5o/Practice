#Function with Return value

def add(a,b):
    c= a+b       # return a+b
    return c     #//


result=add(5,4)
print(result)


print("One More Example")

def formate_name(fname,lname):
    formatted_f_name=fname.title()
    formatted_l_name=lname.title()
    print(f"{formatted_f_name} {formatted_l_name}")


formate_name("XyyZz","NOTHING")



'''
print("Second to way")
def formate_name(fname,lname):
    formatted_f_name=fname.title()
    formatted_l_name=lname.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(formate_name("XyyZz","NOTHING"))
'''

'''
print("Third way ")
print("Store in variable & print)
'''