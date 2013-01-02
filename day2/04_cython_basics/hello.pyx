from libc.stdio cimport printf

def py_sum(a, b):
	return a+b

cdef int c_sum(int a, int b):
	return a+b

def py_hello_to(name):
	print("Hello %s!" % name)

cdef c_hello_to(bytes name):
	cdef char* c_name = name
	printf("Hello %s!", c_name)

def py_c_hello_to(name):
	c_hello_to(name)
