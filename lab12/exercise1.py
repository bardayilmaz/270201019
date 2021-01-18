def selectionSort(l):
	for i in range(len(l)):
		min = l[i]
		for j in range(i+1, len(l)):
			if l[j] < min:
				l[j], l[i] = l[i], l[j]

a = [9,8,7,66,5,4,321,4]
selectionSort(a)
print(a)