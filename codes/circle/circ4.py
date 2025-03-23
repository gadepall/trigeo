#Code by GVV Sharma
#March 23, 2025
#released under GNU GPL


import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/github/trigeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import scipy.linalg as SA
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

#Input parameters
l_1= 5
l_2= 11
d = 6 
r = mp.sqrt(((4*d**2 -l_1**2+l_2**2)/(4*d))**2+l_1**2)/(2)
print(r,5*mp.sqrt(5)/2)
