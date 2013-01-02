import cProfile
import timeit
import random
import numpy as np
import sys

#Note: IPython has some nice magic funtions to make
#profiling even easier. To learn how type
#%quickref
#in Ipython. Look into the commands prun and timeit

def pylist_dgemm(a, b):
    N=len(a)
    M=len(b[0])
    out=[[0]*M for i in xrange(N)]
    #NOTE: A gotcha is [[0]*M]*N, because the outer *N
    #creates only a shallow rather than deep copy

    for i in xrange(N):
        for j in xrange(M):
            pylist_dot(out, a, b, i, j)
    return out

def pylist_dot(out, a, b, i, j):
    for k in xrange(len(b)):
        out[i][j] += a[i][k]*b[k][j]

def np_dgemm(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b)

def rand_list_mat(N):
    a = []
    for i in xrange(N):
        a.append([])
        for j in xrange(N):
            a[-1].append(random.random())
    return a

def main():
    try:
        N = int(sys.argv[1])
        reps = int(sys.argv[2]) 
    except: 
        print "Error"
        print "usage: python program_name matrix_size n_repititions"
        sys.exit() 

    a = rand_list_mat(N)
    b = rand_list_mat(N)

    cProfile.runctx('pylist_dgemm(a,b)', globals(), locals() )
    print '='*80
    
    cProfile.runctx('np_dgemm(a,b)', globals(), locals() )

    print '='*80

    t = timeit.Timer(lambda: pylist_dgemm(a,b))
    print "number repititions: %d" % reps
    print t.timeit(reps)

    print '=' * 80
    t = timeit.Timer(lambda: np_dgemm(a,b))
    print "number repititions: %d" %reps
    print t.timeit(reps)


if __name__ == "__main__":
    main()
