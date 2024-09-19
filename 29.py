'''
Write a program to demostrate the use of positional argument, keyword argument and default argument.
'''

def m_f(fname,lname): # positional argument

    print(fname,lname)

m_f("hellO","how are u")


def m_f(one,two,three): # Keyword argument

    print("Three wala=>",three)

m_f(three="two",two="one",one="three")


def m_f(country="India"):#default argument

    print("My country=>",country)

m_f()
m_f("Bharat")


def m_f(*args): #variable length argument

    print("third argument=>",args[3]) 

m_f(1,2,3,4,5)


