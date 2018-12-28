# =======================
# Importing the libraries
# =======================


import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt



print '------------'
print 'COMPARATION:'
print '------------'

start_time = time()

# -----------
# GHIA et al.
# -----------

x_a = np.zeros([17,1], dtype = float)
v_a = np.zeros([17,1], dtype = float)


x_a[16] = 1.0000
x_a[15] = 0.9688
x_a[14] = 0.9609
x_a[13] = 0.9531
x_a[12] = 0.9453
x_a[11] = 0.9063
x_a[10] = 0.8594
x_a[9] = 0.8047
x_a[8] = 0.5000
x_a[7] = 0.2344
x_a[6] = 0.2266
x_a[5] = 0.1563
x_a[4] = 0.0938
x_a[3] = 0.0781
x_a[2] = 0.0703
x_a[1] = 0.0625
x_a[0] = 0.0000

v_a[16] = 0.00000
v_a[15] = -0.12146 
v_a[14] = -0.15663 
v_a[13] = -0.19254 
v_a[12] = -0.22847
v_a[11] = -0.23827 
v_a[10] = -0.44993 
v_a[9] = -0.38598 
v_a[8] = 0.05186
v_a[7] = 0.30174
v_a[6] = 0.30203 
v_a[5] = 0.28124 
v_a[4] = 0.22965 
v_a[3] = 0.20920 
v_a[2] = 0.19713 
v_a[1] = 0.18360
v_a[0] = 0.00000

# -------------
# MARCHI et al.
# -------------

x_b = np.zeros([17,1], dtype = float)
v_b = np.zeros([17,1], dtype = float)

x_b[16] = 1.0000
x_b[15] = 0.9375
x_b[14] = 0.8750
x_b[13] = 0.8125
x_b[12] = 0.7500
x_b[11] = 0.6875
x_b[10] = 0.6250
x_b[9] = 0.5625
x_b[8] = 0.5000
x_b[7] = 0.4375
x_b[6] = 0.3750
x_b[5] = 0.3125
x_b[4] = 0.2500
x_b[3] = 0.1875
x_b[2] = 0.1250
x_b[1] = 0.0625
x_b[0] = 0.0000

v_b[16] = 0.00000
v_b[15] = -0.27035 
v_b[14] = -0.44901 
v_b[13] = -0.40004 
v_b[12] = -0.28099 
v_b[11] = -0.18210 
v_b[10] = -0.10084
v_b[9] = -0.02471
v_b[8] = 0.05205 
v_b[7] = 0.13057 
v_b[6] = 0.20657 
v_b[5] = 0.26831
v_b[4] = 0.30096
v_b[3] = 0.29747 
v_b[2] = 0.26225 
v_b[1] = 0.18513
v_b[0] = 0.00000


cav_num = []
with open('re400b_vy.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

x = np.zeros([len(cav_num)-1,1], dtype = float)
vy = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vy[i-1] = cav_num[i][2]
 x[i-1] = cav_num[i][8]


end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""


plt.plot(x, vy, '-', color='black', label = "current work")
plt.plot(x_a, v_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(x_b, v_b, 'x', color='black', label = "Marchi et al. (2009)")
plt.legend(loc = 3)
plt.ylabel('v-velocity')
plt.xlabel('x')
plt.show()
