# =======================
# Importing the libraries
# =======================

import sys

import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
#import tikzplotlib


# -----------
# GHIA et al.
# -----------

y_a = np.zeros([17,1], dtype = float)
u_a = np.zeros([17,1], dtype = float)


y_a[16] = 1.0000
y_a[15] = 0.9766
y_a[14] = 0.9688
y_a[13] = 0.9609
y_a[12] = 0.9531
y_a[11] = 0.8516
y_a[10] = 0.7344
y_a[9] = 0.6172
y_a[8] = 0.5000
y_a[7] = 0.4531
y_a[6] = 0.2813
y_a[5] = 0.1719
y_a[4] = 0.1016
y_a[3] = 0.0703
y_a[2] = 0.0625
y_a[1] = 0.0547
y_a[0] = 0.0000

u_a[16] = 1.00000
u_a[15] = 0.84123 
u_a[14] = 0.78871 
u_a[13] = 0.73722 
u_a[12] = 0.68717 
u_a[11] = 0.23151 
u_a[10] = 0.00332 
u_a[9] = -0.13641 
u_a[8] = -0.20581 
u_a[7] = -0.21090 
u_a[6] = -0.15662 
u_a[5] = -0.10150 
u_a[4] = -0.06434 
u_a[3] = -0.04775 
u_a[2] = -0.04192 
u_a[1] = -0.03717 
u_a[0] = 0.00000

# -------------
# MARCHI et al.
# -------------

y_b = np.zeros([17,1], dtype = float)
u_b = np.zeros([17,1], dtype = float)

y_b[16] = 1.0000
y_b[15] = 0.9375
y_b[14] = 0.8750
y_b[13] = 0.8125
y_b[12] = 0.7500
y_b[11] = 0.6875
y_b[10] = 0.6250
y_b[9] = 0.5625
y_b[8] = 0.5000
y_b[7] = 0.4375
y_b[6] = 0.3750
y_b[5] = 0.3125
y_b[4] = 0.2500
y_b[3] = 0.1875
y_b[2] = 0.1250
y_b[1] = 0.0625
y_b[0] = 0.0000

u_b[16] = 1.00000
u_b[15] = 0.59746 
u_b[14] = 0.31055 
u_b[13] = 0.14042 
u_b[12] = 0.02787 
u_b[11] = -0.06024 
u_b[10] = -0.13125
u_b[9] = -0.18208 
u_b[8] = -0.20914 
u_b[7] = -0.21296 
u_b[6] = -0.19847 
u_b[5] = -0.17271
u_b[4] = -0.14193 
u_b[3] = -0.10981 
u_b[2] = -0.07712 
u_b[1] = -0.04197 
u_b[0] = 0.00000

# ---------------------------------------------------
cav_num = []
with open('horizontalProfile.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][1]
 y1[i-1] = cav_num[i][7]
# ---------------------------------------------------
cav_num = []
with open('vxSLwithALE.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][1]
 y2[i-1] = cav_num[i][7]
# ---------------------------------------------------
cav_num = []
with open('TG.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]
# ---------------------------------------------------
cav_num = []
with open('aleTG.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]
# ---------------------------------------------------



plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'Horizontal Velocity',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('auto')
plt.plot(vx1, y1, '-', color='black', label = "Current Work")
#plt.plot(vx3, y3, '-', color='red', label = "TG without ALE")
#plt.plot(vx2, y2, '-', color='black', label = "SL with ALE")
#plt.plot(vx4, y4, '-', color='red', label = "TG with ALE")
plt.plot(u_a, y_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(u_b, y_b, 'x', color='black', label = "Marchi et al. (2009)")
plt.legend(loc = 4)
#tikzplotlib.save("horizontalVelocity.tex")
plt.show()

