n = int(input("type a num for identity matrix: "))
IDMatrix = list()
for i in range(n):
	IDMatrix.append([])
	for j in range(n):
		IDMatrix[i].append(0)
	IDMatrix[i][i] = 1
print(IDMatrix)