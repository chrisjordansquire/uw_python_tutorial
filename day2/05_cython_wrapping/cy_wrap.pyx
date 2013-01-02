import numpy as np
cimport numpy as np
cimport cython

cdef extern int times_row(double *data, int rows, int columns)

@cython.boundscheck(False)
@cython.wraparound(False)
def py_call(np.float64_t[:,::1] data not None):

	cdef int m,n, ret

	m,n = data.shape[0], data.shape[1]

	ret = times_row( <double *> &data[0,0], m, n )
	
	return ret
	
