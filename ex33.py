i = 0
numbers = []

def append_number(step, i):
	while i < 6:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + step;
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i 
	print "The numbers:"
	for num in numbers:
		print num
		
append_number(3, 1)