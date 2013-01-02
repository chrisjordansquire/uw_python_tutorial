import numpy as np
import scipy as sp

#NumPy is very straight-forward
#Like matlab or R, except embedded inside a general purpose
#programming language

#These are only the most basic examples. The online docs show many
#more modules and functions in both numpy and scipy. Generally the
#docs are fairly high quality, so refer to them often when you
#are looking for various functions.

def basics():
    x = np.arange(10)
    print x
    print x.size
    print x.shape
    print

    #Reshape x
    x = x.reshape(2,5)
    print x
    print x.size
    print x.shape
    print

    #y is a view of x, and shares the same underlying data
    #This is desirable behavior because it avoids copies
    #by default.
    y = x.flatten()
    print y
    y[0]=100
    print y
    print x

    #Can easily copy the underlying data
    z=x.copy()
    print

def matrix_ops():
    #the numpy ndarray uses * for elementwise ops
    #there is a separate numpy matrix class where
    #* means matrix multiplications

    x = np.arange(10).reshape(5,2)
    y = np.arange(10).reshape(2,5)
    print np.dot(x,y)
    print np.dot(y,x)
    #x*y is an error
    print

def broadcasting():
    #Arrays can distribute certain elementwise operations
    #over shape indices that are one
    #This can make certain formulas very simple, and also
    #is different behavior from R.

    x = np.array([[1,2],[2,1]])
    y = np.array([3,1]).reshape(1,2)

    w = x+2
    z = x+y

def ufuncs():
    #ufuncs are numpy speak for functions that operate
    #elementwise on numpy ndarrays

    x = np.arange(4).reshape(2,2)
    np.sin(x)

    #the following would be an error because math.sin
    #doesn't know how to operator on numpy classes
    #import math
    #math.sin(x)

def indexing():
    #There are a number of ways to access elements of a
    #numpy array

    x = np.arange(15).reshape(3,5)
    y = x[:,[1,3]]
    z = x[x>3]

def main():
    basics()
    matrix_ops()
    broadcasting()
    ufuncs()
    indexing()

if __name__ == "__main__":
    main()

