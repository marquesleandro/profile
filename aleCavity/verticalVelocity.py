# =======================
# Importing the libraries
# =======================


import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
#import tikzplotlib




# -----------
# GHIA et al.
# -----------

x_a = np.zeros([17,1], dtype = float)
v_a = np.zeros([17,1], dtype = float)


x_a[15] = 1.0000
x_a[14] = 0.9688
x_a[13] = 0.9609
x_a[12] = 0.9531
x_a[11] = 0.9453
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
v_a[15] = -0.05906 
v_a[14] = -0.07391 
v_a[13] = -0.08864 
v_a[12] = -0.10313 
v_a[11] = -0.16914 
v_a[10] = -0.22445 
v_a[9] = -0.24533 
v_a[8] = 0.05454
v_a[7] = 0.17527 
v_a[6] = 0.17507 
v_a[5] = 0.16077 
v_a[4] = 0.12317 
v_a[3] = 0.10890 
v_a[2] = 0.10091 
v_a[1] = 0.09233
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
v_b[15] = -0.12331 
v_b[14] = -0.21869 
v_b[13] = -0.25376 
v_b[12] = -0.22782 
v_b[11] = -0.16301 
v_b[10] = -0.0840
v_b[9] = -0.00774
v_b[8] = 0.05753 
v_b[7] = 0.10877 
v_b[6] = 0.14573 
v_b[5] = 0.16913
v_b[4] = 0.17924
v_b[3] = 0.17434 
v_b[2] = 0.14924 
v_b[1] = 0.09480
v_b[0] = 0.00000


# ---------------------------------------------------
cav_num = []
with open('verticalProfile.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

x = np.zeros([len(cav_num)-1,1], dtype = float)
vy = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vy[i-1] = cav_num[i][2]
 x[i-1] = cav_num[i][8]
# ---------------------------------------------------


plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'x',fontsize=14)
ax.set_ylabel(r'Vertical Velocity',fontsize=14)
ax.set_aspect('auto')
plt.plot(x, vy, '-', color='black', label = "Current Work")
plt.plot(x_a, v_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(x_b, v_b, 'x', color='black', label = "Marchi et al. (2009)")
plt.legend(loc = 3)
#tikzplotlib.save("verticalVelocity.tex")
plt.show()

