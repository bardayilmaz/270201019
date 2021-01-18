def selectionSort(l):
	step = 0
	for i in range(len(l)):
		min = i
		for j in range(i+1, len(l)):
			step += 1
			if l[j] < l[min]:
				min = j
		l[i], l[min] = l[min], l[i]
	print("sort completed in",step,"steps")	
	return l

def binarySearch(element, nums, step = 1):
	print("step!")
	if len(nums) == 0:
		print("could not find. step count:",step)
		return -1

	mid = len(nums) // 2
	item = nums[mid]

	if item == element:
		print("step:",step)
		return mid
	elif element < item:
		return binarySearch(element, nums[:mid], step+1)
	else:
		loc = binarySearch(element, nums[mid+1:], step+1)
		if loc == -1:
			return -1	
		return loc + mid +1	

a = [9,8,3214,32,412,222,7,66,5,4,321,4]

print(binarySearch(3214,selectionSort(a)))