books =  ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookdDict = dict()
for i in range(len(books)):
	tup = ((len(books[i]), len(set(books[i]))))
	bookdDict.update({books[i]: tup})
print(bookdDict)
