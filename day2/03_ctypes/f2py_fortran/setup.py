from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup, Extension

#The shared object library can also be built directly, assuming
#the correct flags are used. It should look something like
#
#gfortran -shared -fPIC -o foo.so kernel_iso_c_binding.f90
#
#This also requires gfortran 4.3
#or later to ensure iso_c_binding is available. Without
#the iso_c_binding the appropriate names would be compiler
#specific, and the easiest thing to do is use numpy's tools or
#write a C wrapper which calls the fortran.

def configuration():
	config = Configuration()
	config.add_extension('foo', sources=['kernel.f90'])

	return config

if __name__ == "__main__":
	setup(**configuration().todict())
