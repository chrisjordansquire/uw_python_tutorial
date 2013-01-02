from distutils.core import setup, Extension

#We can build this library using the setup.py script called as
#python setup.py build
#and then moving the .so file out of the build/lib* directory

#Alternatively, kernel.c can be built into a shared library foo.so
#On linux this can be done with a command like
#gcc -shared -fPIC -o foo.so kernel.c

setup(name="foo", ext_modules=[Extension("foo", ['kernel.c'])] )
