"""
This is a short intro to the basic built-in data structures in Python
"""

#Lists
x = ['a', 1, ['c', 'Jane Austen']] #lists can contain anything
assert(x[0] == 'a') #access list elements w/ 0-indexing
x.append("eep!!!!\n") #can append new items
x[1:3] #returns [x[1], x[2]]

range(1, 10) #creates the list [1,...,8,9]

#List Comprehensions
#These are awesome for quickly creating somewhat complex lists
#This is probably the simplest way to subset a list in more
#complicatd ways than using a slice
[i**2 for i in range(20)]
#IMPORTANT: List comprehensions work for ANY iterable, not just lists.
#We'll see examples of this later

#Everything in python is an object
#You can see a list's methods, or any object's methods, by calling dir
#Such as dir(x)
#If you forget what a method does, you can easily find out (in the REPL)
#by calling help, such as help(x.count).

#Tuples
y = ('a', 'b', ['c','d']) #A tuple is a list variant
#You can't reassign any element of a tuple
#In that sense a tuple is immutable
#So
#xx[0] = 'e'
#is illegal
y[2].append('e') #But a tuple's elements can still be mutable


#Dictionaries
#A dictionary, called a map or associative container in other languages,
#associates a key with a value. So if d is a dictionary then assigment
#works as d[key] = value and d[key] returns the value associated to key.
#Note: The key must be an immutable type. So numbers, strings, and tuples
#are ok as keys, but lists are not.
z = {'a':1, 2:'b', ('e','d'):[7,8,9]}

#Can access keys, values, and (key, value) tuples
z.keys()
z.values()
z.items()

#The below would raise a KeyError
#z[10]
#A key error is raised whenever a dict doesn't contain anything
#for the given key
#There are two ways to get around this: z.get and z.has_key
z.has_key(10)
z.get(10, 'NCIS')

#There are also dictionary comprehensions
{i:i**2 for i in range(5)}

#Sets
#These data structures model a set.
w = set(range(4))
2 in w
w.add(0)
#You can also take unions, intersections, differences, etc. w/ sets
#There are also set comprehensions
v = {x for x in range(4)}
v.add(0)

#There are many variants of the above in the collections library
#in the python standard library. Take a look at the docs online.
