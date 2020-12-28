def recursiveMultiplication(n, count = 0, n_ = 0):
	
	if count == 0:
		n_ = n
	if count == 2:
		print(n)
	else:
		return recursiveMultiplication(n+n_, count+1, n_)
def func2(n):
	if n == 1:
		return 3
	else:
		return 3 + func2(n-1)			

recursiveMultiplication(6)		
print(func2(5))	