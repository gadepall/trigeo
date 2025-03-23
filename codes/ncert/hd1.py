#Code by GVV Sharma
#March 22, 2025
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
h = 3400
t = 10
theta_deg = 30
v = (h*np.deg2rad(theta_deg))/t
print(v)

