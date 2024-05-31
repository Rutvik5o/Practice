gradeDict={

    'kelly':[90,44],
    'daivd':88,
    'hdhh':87,
}

print(gradeDict)

print(gradeDict['hdhh']) #through specific key which we can know value

gradeDict['daivd']=55

print(gradeDict)

del gradeDict['hdhh'] #=> delete that key & value

print(gradeDict['kelly'])

print(gradeDict['kelly'][1])