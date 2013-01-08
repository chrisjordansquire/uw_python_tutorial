import hello as h

def main():
    #Note that the cdef'd functions are not visible to python
    print dir(h) 
   
    print h.py_sum(3,4)
    print h.py_hello_to("BLDF") 
    print h.py_c_hello_to("Alex Martelli") 

if __name__ == "__main__":
    main() 
