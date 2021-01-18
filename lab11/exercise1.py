class Cylinder:
	def __init__(self, radius, height):
		self.radius = radius
		self.height = height

	def get_radius(self):
		return self.radius
	def set_radius(self, radius):
		if radius > 0:
			self.radius = radius

	def get_height(self):
		return self.height
	def set_height(self, height):
		if height > 0:
			self.height = height
			
	def surface_area(self):
		return 2*3.14*self.height*self.radius

	def base_area(self):
		return 3.14*(self.radius)**2		

	def calculate_area(self):
		baseArea = self.base_area()
		surfaceArea = self.surface_area()
		return 2*baseArea + surfaceArea

	def calculate_volume(self):
		baseArea = self.base_area()
		return baseArea * self.height


cylinder1 = cylinder(3,5)
print(cylinder1.calculate_area())
print(cylinder1.calculate_volume())		

		

						