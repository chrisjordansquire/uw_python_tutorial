from libc.stdio cimport printf

#simple examples
#check out the generated C code and compare

def py_sum(a, b):
    return a+b

def py_sum_int(int a, int b):
    return a+b

cdef int c_sum(int a, int b):
    return a+b

def py_hello_to(name):
    print("Hello %s!" % name)

cdef void c_hello_to(char* c_name):
    printf("Hello %s!", c_name)

#Should use cpdef instead of wrapping the cdef. 
#That's quicker and safer than wrapping yourself. 
#The wrapper will still have the python-cython conversion
#overhead, but there's no way around that. 

#Also, 'bytes' is python's version of a char*...I think
def py_c_hello_to(bytes name):
    #cython automatically converts the python string to a char*
    cdef char* c_name = name
    c_hello_to(c_name)

#Slightly more complex example

def sum_list(list):
    sum = 0
    for i in list:
        sum+= i
    return sum

cdef int c_sum_list(int ilist[], int n):
    cdef int sum=0
    for i in range(n):
        sum += ilist[i]
    return sum

