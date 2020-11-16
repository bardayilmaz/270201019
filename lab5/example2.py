numCount = int(input("How many numbers will you enter? "))
evenCount = 0
for _ in range(numCount):
	num = int(input("type a num: "))
	if num % 2 == 0:
		evenCount+=1
print(evenCount/numCount*100,"%")		