def isPrime(num):
	if num < 2:
		return False
	for i in range(2,num//2):
		if num % i == 0:
			return False
	return True

def primesBetween(a,b):
	primeList = []
	for i in range(a,b):
		if isPrime(i):
			primeList.append(i)
	print(primeList)

def main():
	x = int(input("num1: "))
	y = int(input("num2: "))
	primesBetween(x,y)

main()