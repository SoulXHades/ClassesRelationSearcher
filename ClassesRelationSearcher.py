import os

fd = open(input("Input class list directory: "), "r")
listOfClasses = fd.readlines();

fd1 = open(input("Input programming file directory: "), "r")
listofCodes = fd1.readlines();

listOfClassesExistsInCode = []


for rowsOfCode in listofCodes:
	for eachclass in listOfClasses:
		if eachclass[:-2] in rowsOfCode[:-2]:
			if eachclass not in listOfClassesExistsInCode:
				listOfClassesExistsInCode.append(eachclass)

for eachClassesExistsInCode in listOfClassesExistsInCode:
	print(eachClassesExistsInCode)


fd.close()
fd1.close()