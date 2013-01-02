"""
Objects...sigh....
"""

#Good news: Python has much better support for objects than matlab
#or R. And unlike those archaic languages, it wasn't bolted on as
#an afterthought. This allows for a lot of win in terms of
#nicely organizing code.

#Bad news: Good object oriented design is hard. Objects are easy
#to overuse and abuse. General advice is to prefer composition
#over inheritance, the Liskov substitution principle, and to just
#not use objects unless they clean up your code.
#Jack Diederich has an excellent PyCon talk on not misusing objects.

#So, without further ado, here are two examples of objects, and
#a simple function using them.

class vector(object):

	def __init__(self, iterable):
		self.vec = [x for x in iterable] #local copy

	def __add__(self, other):
		assert(len(self.vec) == len(other))
		return [x+y for x,y in zip(self.vec, other)]

	def _radd__(self, other):
		return self+other

	def __iadd__(self, other):
		assert(len(self.vec) == len(other))
		for i in xrange(len(self.vec)):
			self.vec[i] = self.vec[i] + other[i]
		return self

	def __contains__(self, value):
		return value in self.vec

	def __str__(self):
		return str(self.vec)

	def __len__(self):
		return len(self.vec)

	def append(self, new_elem):
		self.vec.append(new_elem)

#Note: there are no true private methods or variables in an object.
#A single underscore is the traditional way of indicating something
#is meant to be private. Double underscores should be avoided.

#Since there are no truly private variables, there isn't much point
#in writing getters and setters for variables. Which isn't good
#practice anyways.

def main():
	x = [2*i+1 for i in range(5)]
	y = [3*i for i in range(5)]

	v = vector(x)
	print len(v)
	print v
	print v+y
	#print y+v
	#Above doesn't work because __add__ is defined for lists
	y[0]=12
	v+=y
	print v
	v.append(20)
	print v


if __name__ == "__main__":
	main()
