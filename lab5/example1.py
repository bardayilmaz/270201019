intInput = int(input("type an int between 0 and 11: "))
while intInput <= 0 or intInput >10:
	print("please enter a valid number!")
	intInput = int(input("type an int between 0 and 11: "))

for i in range(1, 11, 1):
	print(intInput, "x", i, "=", + intInput*i)