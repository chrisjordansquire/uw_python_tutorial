"""
Short intro to functions.....finally.....
"""

#Defining a function is easy
def g():
	print "Hello, functions!"

#Calling a function is easy
g()

#Arguments are easy
def g_with_args(x1, x2):
	print x1
	print x2

#Return a value...heck, return multiple values

def rotate(a,b):
	return a+b, a-b

#Note that returning multiple values returns a tuple
#Tuples are automatically unpacked, as follows

x,y = rotate(2,1)
print x,y

#This alone fills one with fanatical devotion to the BDFL

#Can also access varaibles by their names
x2, y2 = rotate(b=1, a=2) #Same as above call
print x2, y2

#Scope in python functions is local
#you can't access outside variables nor can variables
#defined within the function be accessed outside
#BUT, mutable variables can be mutated within the function
#and these changes will be visible outside the function

#Also, you can give default arguments to a function
def h(x, y, z="Twilight Sparkle"):
	x+= 1 #this change does not appear outside h
	y.append("item "+str(x)) #this change is visible outside h
	print z



