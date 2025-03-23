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
d2 = 20
theta1= np.deg2rad(60)
theta2= np.deg2rad(30)
A = np.array([[mp.cot(theta2), -1],[mp.cot(theta1), -1 ]],dtype=float)
b = np.array([1,0]).reshape(-1,1)
print(A,b,d2*LA.solve(A,b))

