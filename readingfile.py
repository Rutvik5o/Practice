readMe= open("examplewrite.txt",'r').read()

print(readMe)

spiltMe=readMe.split("\n")

#print(splitMe[1])

print(spiltMe)

readMe2=open("examplewrite.txt",'r').readlines()

print(readMe2)