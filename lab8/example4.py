def binaryToDecimal(num):
	num = str(num)
	decimal = 0
	for i in range(len(num)):
		if num[i] == "1":
			decimal += 2**(len(num)-(i+1))
	print(decimal)

def decimalToBinary(num):
	b = ""
	binary = ""
	while num > 0:
		b += str(num%2)
		num //= 2
	return b[::-1]	


binaryToDecimal(1101)	
print(decimalToBinary(18))		