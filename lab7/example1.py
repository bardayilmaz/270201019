ageDict = {"Jon": 15, "Ned":45, "Arya":9, "Catelyn":44, "Bran":10}
for person in ageDict:
	if ageDict.get(person) > 18:
		print(person)