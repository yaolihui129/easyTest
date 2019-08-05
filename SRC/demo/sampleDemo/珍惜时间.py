import time
i=29548800   #assuem how many seconds you can live in this world
for a in range(0,i):
	c=i-a
	time.sleep(0.5)
	print("Your life in the world has %d seconds left, Value your time" %c)
	time.sleep(0.5)
	i=i-1
exit(0)