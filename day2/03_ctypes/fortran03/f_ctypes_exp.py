import ctypes as c
import os
import os.path
import numpy as np

cur_dir = os.getcwd()
so_filename = os.path.join(cur_dir, 'foo.so')

_foo = c.CDLL(so_filename)
_foo.addtwo_real.restype = c.c_double

def c_int_ref(x):
	return c.byref(c.c_int(x))

def c_double_ref(x):
	return c.byref(c.c_double(x))

def mult(a,b):
	a = c_int_ref(a)
	b = c_int_ref(b)
	return _foo.multiply(a, b)

def addtwo(a,b):
	a = c_int_ref(a)
	b = c_int_ref(b)
	return _foo.addtwo(a,b)

def addtwo_real(a,b):
	a = c_double_ref(a)
	b = c_double_ref(b)
	return _foo.addtwo_real(a,b)


print "should be 20: " + str(mult(2,5))
print "should be 12: " + str(addtwo(3,9))
print"should be 25: " + str(addtwo_real(20,5))

_foo.times_row.argtypes = [c.POINTER(c.c_double),
        c.POINTER(c.c_int), c.POINTER(c.c_int)]

def bar(x, rows, columns):
    rows = c_int_ref(rows)
    columns = c_int_ref(columns)
    return _foo.times_row(x.ctypes.data_as(c.POINTER(c.c_double)),
            rows, columns)

x = np.arange(12, dtype='float64')
x = x.reshape(3,4)
print x
bar(x, x.shape[0], x.shape[1])
print
print x

