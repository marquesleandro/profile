# =======================
# Importing the libraries
# =======================


import numpy as np
from time import time
import matplotlib.pyplot as plt



print '------------'
print 'COMPARATION:'
print '------------'

start_time = time()

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
u_a[15] = 0.65928 
u_a[14] = 0.57492 
u_a[13] = 0.51117 
u_a[12] = 0.46604 
u_a[11] = 0.33304 
u_a[10] = 0.18719 
u_a[9] = 0.05702 
u_a[8] = -0.06080 
u_a[7] = -0.10648 
u_a[6] = -0.27805 
u_a[5] = -0.38289
u_a[4] = -0.29730 
u_a[3] = -0.22220 
u_a[2] = -0.20196 
u_a[1] = -0.18109 
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
u_b[15] = 0.42229 
u_b[14] = 0.36254 
u_b[13] = 0.28844 
u_b[12] = 0.20791 
u_b[11] = 0.13357 
u_b[10] = 0.06524
u_b[9] = 0.00056 
u_b[8] = -0.06205 
u_b[7] = -0.12341 
u_b[6] = -0.18373 
u_b[5] = -0.24569
u_b[4] = -0.31894 
u_b[3] = -0.38440 
u_b[2] = -0.34784 
u_b[1] = -0.20233 
u_b[0] = 0.00000


cav_num = []
with open('re1000_vx.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y = np.zeros([len(cav_num)-1,1], dtype = float)
vx = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx[i-1] = cav_num[i][1]
 y[i-1] = cav_num[i][7]


end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""


plt.plot(vx, y, '-', color='black', label = "trabalho atual")
plt.plot(u_a, y_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(u_b, y_b, 'x', color='black', label = "Marchi et al. (2009)")
plt.legend(loc = 4)
plt.ylabel('y')
plt.xlabel('u-velocidade')
plt.show()
