itemCount = int(input("How many element will you enter? "))
usersList = list()
uniqueList = list()
counter = 0
for i in range(itemCount):
	usersList.append(input(f"{i+1}. element: "))
for i in range(itemCount):
	if not usersList[i] in uniqueList:
		uniqueList.append(usersList[i])
print(usersList,"\n",uniqueList)		