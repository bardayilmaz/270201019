from random import sample

def intersection(list1, list2):
	intersectionList = list()
	for i in list1:
		if i in list2 and not i in intersectionList:
			intersectionList.append(i)	
	return intersectionList			

def main():
	b = 1
	e = 10	
	N = 5
	list1 = sample(range(b,e),N)
	list2 = sample(range(b,e),N)
	print("list1:", list1)
	print("list2:", list2)
	print("intersection:", intersection(list1,list2))

main()