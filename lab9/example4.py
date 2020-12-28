from time import sleep
def timer(t):
	if t == -1:
		print("TIME IS UP!")
		return 0
	else:
		sleep(1)
		if t != 0:
			print(str(t)+"...")
		timer(t-1)
timer(6)
		
