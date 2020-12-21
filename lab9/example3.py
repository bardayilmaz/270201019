def evenCount(lst,count = 0):
	if len(lst) == 0:
		return count
	else:
		if lst[-1] % 2 == 0:
			count += 1
		return evenCount(lst[:-1], count)		
a = [1,2,3,4,5,6,0,0]
print(evenCount(a))