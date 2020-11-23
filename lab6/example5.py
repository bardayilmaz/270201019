n = int(input("length of the square: "))
matrix = list()
trace = 0
for i in range(n):
	matrix.append([])
	for j in range(n):
		matrix[i].append(int(input(f"{j+1}. element of {i+1}. line: ")))
	trace += (matrix[i][i])	
print(matrix)
print(trace)
