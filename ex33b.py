i = 0 
x = 6
numbers = []

def test(i):
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

test(0)

print "The numbers: "

for num in numbers:
	print num
