def recursiveMultiplication(n, count = 0, n_ = 0):
	if count == 0:
		n_ = n
	if count == 2:
		print(n)
	else:
		return recursiveMultiplication(n+n_, count+1, n_)

recursiveMultiplication(5)			