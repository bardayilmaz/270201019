def hailstone(n):
	s = str(n)
	print(s+", ", end = "")
	if n == 1:
		return 1
	elif n%2 == 0:
		return hailstone(n//2)
	else:
		return hailstone(3*n + 1)

hailstone(11)