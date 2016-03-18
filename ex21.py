def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTNG %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a / b
	
print "Lets do some math with just functions"

age = add(40, 2)
height = subtract (78, 4)
weight = multiply(110, 2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ %d" % (age, height, weight, iq)
		
print "here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "The becomes: ", what, "can you do it by hand?"