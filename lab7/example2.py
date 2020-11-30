books =  ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookdDict = dict()
bookLen = 0
uniqueLen= 0
for i in range(len(books)):
	bookLen = len(books[i])
	uniqueLen = len(set(books[i]))
	tup = (bookLen, uniqueLen, (bookLen+uniqueLen)/2)
	bookdDict.update({books[i]: tup})
print(bookdDict)
