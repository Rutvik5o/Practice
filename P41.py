# Sets

set1={10,36,39,59,"Hey",True}

set2={}  #-> It's Dictionary

print(type(set1))

print(type(set2))

print(set1)


# For Add value on set

set1={45,49}

set1.add(101)

print(set1)

print(len(set1))

print("Remove Also Possible")

set1.remove(101)

print(set1)

print("Discard")

set1.discard(10)

print(set1) #->If you discard any value which Not on set there it's not give error.

set1.clear()

print(set1)

# For Remove any random vallue

set1={49,359,'hey',True,False,99}

print(set1.pop()) #-> Its's disply removed value

print(set1)

#We can add tuple on set Bcoz tuple are immutable.

#We can't add list because it's mutable {we can change the data}.


#Operations(2)

set1={10,14,52,39}

set2={14,52,45,39,10}

set3={69,359,39,35}

print(set1.union(set2))

print(set1.union(set2,set3))

#-> We can also union with tuple

print(set1.union(('Xyz',"Welcome")))

print(set1 | set2)

#-> Update

set1.update(['Hello',"xyz"])

print(set1)

#->Intersection

print(set1.intersection(set2))

print(set1 & set2 & set3)

print(len(set1 & set2 & set3))

#->Intersection Update

set1.intersection_update(set2)

print(set1)

set2.intersection_update(set1)

print(set1)

print(set2)

#(3)

set1={'Hey','Xyz','Mno'}

set2={"Mno","Xyz","Poy"}

set3={'Ankur',"Xyz",'Mno'}

print(set1.difference(set2,set3))

print(set1 - set2)

set2.difference_update(set1)

print(set1)

print(set2)

print(set1.symmetric_difference(set2)) #-> Print all exp common, Not allow multiple

print(set1 ^ set2 ^ set3) #-> Here nultiple allow.

set1.symmetric_difference_update(set2)

print(set1)

#(4)

set1={1,2,3,4,8}

set2={4,10,-7,8,1,2}

print(set1.isdisjoint(set2)) #-> its print true if both are differnt value

print(set1.issubset(set2)) #-> its print true if there subset of that.

#-> Set1 is subset of set2 if every element of set1 is in set2.

#-> Set1 is superset of set2 if set1 contains every elemnt in set2.

set3={3,4}

set4={5,3,5,4}

print(set3.issubset(set4)) #-> Every element of set2 on set1

# For clear

set3.clear()

print(set3)

# For delete set

del set3 #-> its delete it










