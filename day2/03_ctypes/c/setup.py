from distutils.core import setup, Extension

#We can build this library using the setup.py script called as
#python setup.py build
#and then moving the .so file out of the build/lib* directory

#Alternatively, kernel.c can be built into a shared library foo.so
#On linux this can be done with a command like
#gcc -shared -fPIC -o foo.so kernel.c

#However you might need to get some of the compile flags right,
#if the python you're using was compiled with different options
#or for a different architecture than is your default. 
#(For example, I'm using the 32-bit EPD on my 64-bit mac)
#To get the compile flags for the version of python you're running
#call 
#import sysconfig
#sysconfig.get_config_vars()
#That gives a (large) dictionary of configuration variables, 
#including CFLAGS

setup(name="foo", ext_modules=[Extension("foo", ['kernel.c'])] )
