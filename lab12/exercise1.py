def selectionSort(l):
	for i in range(len(l)):
		min = i
		for j in range(i+1, len(l)):
			if l[j] < l[min]:
				min = j
		l[i], l[min] = l[min], l[i]
	return l	

a = [9,8,3214,32,412,222,7,66,5,4,321,4]

print(selectionSort(a))