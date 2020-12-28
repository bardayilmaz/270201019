def hailstone(n):
	if n == 1:
		return int(n)
	elif n%2 == 0:
		return hailstone(n/2)
	else:
		return hailstone(3*n + 1)

print(hailstone(11))			