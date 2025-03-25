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
a_1= 8 
a_2= 6
r =  4
#Intermediate parameters
a = a_1+a_2
B = 2*mp.atan((r)/(a_1))
C = 2*mp.atan((r)/(a_2))
A = mp.pi - B-C
#Output parameters
b = a*mp.sin (B)/mp.sin (A)
c = a*mp.sin (C)/mp.sin (A)
print(b,c)
