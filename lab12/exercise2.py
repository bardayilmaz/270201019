def binarySearch(element, nums):

    if len(nums) == 0: 
        return -1
    mid = len(nums)//2
    item = nums[mid]

    if item == element:
        return mid
    elif element < item: 

        return binarySearch(element, nums[:mid])
    else: 

        return binarySearch(element, nums[mid+1:]) + mid +1

a = [4, 4, 5, 7, 8, 9, 32, 66, 222, 321, 412, 3214]
print(binarySearch(412,a))