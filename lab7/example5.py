numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
setNums1 = set(numbers1)
setNums2 = set(numbers2)
interSet = set()
unionSet = set(numbers1+numbers2)
for i in setNums1:
	if i in setNums2:
		interSet.add(i)
for j in setNums2:
	if j in setNums1:
		interSet.add(j)
print(interSet)
print(unionSet)		