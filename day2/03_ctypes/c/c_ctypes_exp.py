import numpy as np
import ctypes as c
import os
import os.path


cur_dir = os.getcwd()
so_filename = os.path.join(cur_dir, 'foo.so')

_foo = c.CDLL(so_filename)
_foo.times_row.restype = c.c_int
_foo.times_row.argtypes = [c.POINTER(c.c_double), c.c_int, c.c_int]

def bar(x, rows, columns):
	return _foo.times_row(x.ctypes.data_as(c.POINTER(c.c_double)),
			rows, columns)


x = np.arange(12)*1.0 #breaks if not times 1.0, b/c dtype is wrong
x = x.reshape(3,4)
print x
bar(x, x.shape[0], x.shape[1])
print
print x
