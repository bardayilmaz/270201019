def binarySearch(element, nums):
	if len(nums) == 0:
		return -1

	mid = len(nums) // 2
	item = nums[mid]

	if item == element:
		return mid
	elif element < item:
		return binarySearch(element, nums[:mid])
	else:
		loc = binarySearch(element, nums[mid+1:])
		if loc == -1:
			return -1
		return loc + mid +1				

  

a = [4, 4, 5, 7, 8, 9, 32, 66, 222, 321, 412, 3214]
print(binarySearch(3121,a))