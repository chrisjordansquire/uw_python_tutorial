from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

ext_modules = [Extension("cy_wrap",
						sources=["cy_wrap.pyx", "kernel.c"],
						include_dirs=[np.get_include()] ) ]

setup(
        name = "Wrap C Example",
        cmdclass = {'build_ext':build_ext},
        ext_modules = ext_modules
)
