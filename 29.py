def m_f(fname,lname): #positinal arguments

    print(fname,lname)


m_f("one","two")

#keyword arguments


def m_f(one,two,three):

    print("the highest is =>",three)

m_f(three="high",two="low",one="medium")


#default arguments

def m_f(country="India"):

    print("i am from "+country)


m_f()
m_f("Bharat")