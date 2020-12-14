def squareOfSum(numList):
	sum = 0
	for i in numList:
		sum += i
	return sum**2

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(squareOfSum(a_list))