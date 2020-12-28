def sumofNestedList(x):
	if not isinstance(x, list):
		return x
	else:
		sumResult = 0
		for item in x:
			sumResult += sumofNestedList(item)
		return sumResult
		
a_list = [3,12,76, [ 4, 56, 43], [2,8],81,75]
print(sumofNestedList(a_list))
