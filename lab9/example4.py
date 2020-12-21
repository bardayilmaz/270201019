from time import sleep
def timer(t):
	if t == 0:
		return 0
	else:
		sleep(1)
		print(str(t)+"...")
		timer(t-1)
timer(5)
		
