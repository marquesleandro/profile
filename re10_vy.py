# =======================
# Importing the libraries
# =======================

import sys
sys.path.insert(0, '../../lib_class')

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg
import scipy.linalg
import trimsh
import trielem
from tricond import b_bc
import InOut
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt


print '------------'
print 'IMPORT MESH:'
print '------------'

start_time = time()

name_mesh = 'malha_cavity.msh'
mesh = trimsh.Linear('../../mesh',name_mesh)
mesh.parameters(3)
mesh.ien()
mesh.coord()

end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""


print '------------'
print 'COMPARATION:'
print '------------'

start_time = time()

# -----------
# GHIA et al.
# -----------

y_a = np.zeros([17,1], dtype = float)
u_a = np.zeros([17,1], dtype = float)

'''
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
'''
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
v_b[15] = -0.09640 
v_b[14] = -0.15989 
v_b[13] = -0.18702 
v_b[12] = -0.18163 
v_b[11] = -0.15162 
v_b[10] = -0.10561
v_b[9] = -0.05104 
v_b[8] = 0.00636 
v_b[7] = 0.06210 
v_b[6] = 0.11214 
v_b[5] = 0.15205
v_b[4] = 0.17641
v_b[3] = 0.17878 
v_b[2] = 0.15254 
v_b[1] = 0.09297
v_b[0] = 0.00000


cav_num = []
with open('re10_vy.csv') as cav:
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
#plt.plot(u_a, y_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(x_b, v_b, 'x', color='black', label = "Marchi et al. (2009)")
plt.legend(loc = 3)
plt.ylabel('v-velocity')
plt.xlabel('x')
plt.show()
