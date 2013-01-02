#must first run
#python setup.py build
#and then move the .so file in build/lib*/, where the directory lib*
#depends on the architecture of the machine

import foo
import numpy as np

m_ = foo.foo
a = 2
b = 10

print "should be 20: " + str(m_.multiply(a, b))
print "should be 12: " + str(m_.addtwo(a,b))

a = 5
b = 20

print "should be 25: " + str(m_.addtwo_real(a,b))

#Compared to using iso_c_binding, we must be more careful about
#types and layout
#A real in fortran is 32-bit float, so the dtype must match.
#Also, since the fortran code assumes a 1-D array we must pass in
#a 1-D array. This is a benefit and drawback compared to
#ctypes+iso_c_binding, resulting from f2py knowing about numpy arrays.

x = np.arange(12, dtype='float32')
print x.reshape(3,4)
m_.times_row(x, 3, 4)
print
print x.reshape(3,4)

#Note that you can also use ctypes without iso_c_binding. But there are some
#caveats. First is you need to get the compilations flags right. Assuming
#that's done, then you have a shared object library. When I imported
#it using ctypes the fortran functions didn't show up using dir...
#but if you run
#nm foo.so
#you can find out how the fortran compiler mangled the function names.
#In my case it was __foo__multiply, for the multiply function. Then
#I could call it like this:
#
#import ctypes as c
#m = c.CDLL('foo.so')
#m.__foo__multiply(c.byref(c.c_int(20)), c.byref(c.c_int(4)))
#
#That sort of code would be non-portable since it depends on the
#name mangling that the fortran compiler does. For example, the
#name mangling scheme above is from gfortran 4.2.3 on my macbook, but
#ifort version 12.1.5 and gfortran 4.6.3 on my linux desktop both
#produce different manglings.


