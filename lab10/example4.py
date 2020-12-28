def fibonacci(lineNo, currentLine = 1, line= list(), allLines = list()):
	if currentLine == 1:
		line = [1]
		allLines.append(line)
		return fibonacci(lineNo, currentLine+1, line)

	elif currentLine == lineNo+1:
			return allLines
	else:
		newLine = list()
		for i in range(currentLine):
			newLine.append(0)

		for i in range(len(line)):
			if i == 0:
				newLine[0] = 1
			else:
				newLine[i] += line[i]+line[i-1]
		newLine[-1] = 1
		allLines.append(newLine)
		return fibonacci(lineNo, currentLine+1, newLine)

		

print(fibonacci(5))				

