num = input("type a number: ")
if len(num) >= 2:
	digit1 = int(num[len(num)-1])
	digit2 = int(num[len(num)-2])
	print(digit1+digit2)
elif len(num) == 1:
	digit = int(num)
	print(digit)