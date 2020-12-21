def reverse(n,actualList,newList):
	if n == 0:
		return 0
	else:
		newList.append(actualList[-len(actualList)+n-1])
		return reverse(n-1,actualList,newList)	
	
a = [1,2,3,4,5,6]
b = list()
reverse(len(a),a,b)
print(b)		