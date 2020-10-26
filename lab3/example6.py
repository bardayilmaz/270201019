a = int(input("type a for ax^2 + bx + c: "))
b = int(input("type b for ax^2 + bx + c: "))
c = int(input("type c for ax^2 + bx + c: "))
discriminant = b**2 - 4*a*c

if discriminant > 0:
	x1 = (-1*b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-1*b - (b**2 - 4*a*c)**0.5) / (2*a)
	print(f"first root is {x1} and the second is {x2}")
elif discriminant == 0:
	x1 = (-1*b + (b**2 - 4*a*c)**0.5) / (2*a)
	print(f"the only root is {x1}")
else:
	print("there is not a rational root!")	