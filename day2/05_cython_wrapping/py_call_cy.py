import numpy as np
import cy_wrap

x = np.arange(12)*1.0 #breaks if not times 1.0, b/c dtype is wrong
x = x.reshape(3,4)
print x
cy_wrap.py_call(x)
print
print x
