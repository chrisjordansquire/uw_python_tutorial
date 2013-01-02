
#Decorators are a nifty way to easily wrap an existing
#function with something extra. There are a bunch of things
#the something extra could be. Some libraries use decorators
#all over the place, other libraries strenuously avoid them.
#Regardless, like generators they're a nifty trick to have
#up your sleeve.

class counter(object):

	def __init__(self, func):
		self.func = func
		self.counter = 0

	def __call__(self, *args, **kwargs):
		self.counter += 1
		return self.func(*args, **kwargs)

@counter
def fib(n):
	if n==1:
		return 1
	if n==2:
		return 1
	return fib(n-1) + fib(n-2)

class memoize(object):

    def __init__(self, f):
        self.cache={}
        self.f = f

    def __call__(self, *args, **kwargs):
        if (args, str(kwargs)) in self.cache:
            return self.cache[args,str(kwargs)]

        tmp = self.f(*args, **kwargs)
        self.cache[args,str(kwargs)] = tmp
        return tmp

@memoize
def fibc(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fibc(n-1)+fibc(n-2)

def main():

	print fib(30)
	print fib.counter

	print

	print fibc(30)
	print fibc.cache

if __name__ == "__main__":
	main()
