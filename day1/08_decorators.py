
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
    #This is a fairly general memoization decorator class
    #That's why the intenral dictionary is key'd on the tuple
    #combination of args and str(kwargs)
    #But this isn't space efficient if there are no keyword args. 
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
def fibm(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fibm(n-1)+fibm(n-2)

def main():

    print fib(30)
    print "Number of calls to fib: " + str(fib.counter)

    print

    print fibm(30)
    print "The contents of fibm's cache:"
    print fibm.cache

if __name__ == "__main__":
    main()
