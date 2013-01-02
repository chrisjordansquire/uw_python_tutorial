import math
import sys

#Generators are basically lazily-evaluated iterables.
#This means the next item isn't computed until something asks for it.
#The same functionality could be implemented using an object
#with state, but generators allow for eliminating the overhead
#of creating an object.

#Point of the lazy evaluation is several fold. First, it's a great
#abstraction for sequentially processing infinite data. Second,
#it's a good way to avoid doing work you don't need to do when
#doing sequential processing. And third, it can help spread out
#computation time so that things are computed only when you need
#them instead of all up-front.

#Generators can be great for setting up pipelines for processing
#data. David Beazley has a couple of great talks on this.

#Simple example of a generator function
def primeGenerator():
	primes=[2]
	cur=2
	while True:
		cur+=1
		is_prime=True
		for x in primes:
			if x>math.sqrt(cur):
				break
			if cur%x==0:
				is_prime=False
		if is_prime:
			primes.append(cur)
			yield cur


#The simplest way to make a generator is using generator expressions.
def genExpr():
	x = (x**2 for x in range(5)) #Utterly trivial example to show syntax
	for i in x:
		print i


#Example use
def main():
	nPrimes = int(sys.argv[1])

	pGen = primeGenerator()
	for i in range(nPrimes):
		print pGen.next()

	print
	genExpr()

if __name__ == "__main__":
	main()
