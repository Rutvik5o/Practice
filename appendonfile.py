appendMe= "some txt"

saveFile=open('examplewrite.txt','a')

saveFile.write("\n")

saveFile.write(appendMe)

saveFile.close()