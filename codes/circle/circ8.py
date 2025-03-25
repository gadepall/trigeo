#Code by GVV Sharma
#March 25, 2025
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
l= 8 
r = 5
#Intermediate parameters
theta = 2*mp.asin(l/(2*r))
T = mp.pi - theta
#Output parameters
x = (l/2)*mp.sec(theta/2)
print(x)
