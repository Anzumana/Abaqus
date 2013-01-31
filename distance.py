import sys,math
#-------------------------------------------------
def distance(x,y) :
	"""
	Prints distance from origin to (x,y).
	Using Pytagoras c = sqrt(a**2+b**2)

	"""
	# Square the argumnts and add them.
	
	a = x**2 + y**2

	# Return the square root.

	return math.sqrt(a)

# Retrieve the command line arguemtns and 
# converte the string to floating-point numbers.


x = float(sys.argv[1])
y = float(sys.argv[2])

# Call the distance function.

d = distance(x,y)

#Print the result.

print 'Distance to origin =', d
