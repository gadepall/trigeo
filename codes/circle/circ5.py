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
l_1= 6 
l_2= 8
d_1 = 4 

#Intermediate parameters
theta_1 = mp.atan((l_1)/(2*d_1))
theta_2 = mp.asin(l_2*mp.cos(theta_1)/(2*d_1))

#Output parameters
d_2 = (l_2)/(2)*mp.cot(theta_2) 
print(d_2)
