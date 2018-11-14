# =======================
# Importing the libraries
# =======================

import sys
sys.path.insert(0, '/home/marquesgesar/fem/lib_class')

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
print 'COMPARATION:'
print '------------'

start_time = time()

# -----
# 0.1 s
# -----

cav_num = []
with open('poiseulle_20d.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][1]
 y1[i-1] = cav_num[i][7]

# -----
# 0.2 s
# -----

cav_num = []
with open('poiseulle_40d.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][1]
 y2[i-1] = cav_num[i][7]


# -----
# 1 s
# -----

cav_num = []
with open('poiseulle_200d.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]

# ------------
# Steady State
# ------------

cav_num = []
with open('poiseulle_1500d.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]


# -----
# exact
# -----
vxe = np.zeros([200,1], dtype = float)
ye = np.zeros([200,1], dtype = float)

u_max = 1.5
L = 1.0
for i in range(0,200):
 ye[i] = (i/200.0)
 vxe[i] = ((4.0*u_max*ye[i])/L**2)*(L - ye[i])



end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""


plt.plot(vx1, y1, '2', color='black', label = "t = 0.1")
plt.plot(vx3, y3, '.', color='black', fillstyle='none', label = "t = 1.0")
plt.plot(vx4, y4, '-', color='black', label = "solucao numerica")
plt.plot(vxe, ye, '--', color='black', label = "solucao analitica")
plt.legend(loc = 3)
plt.ylabel('y')
plt.xlabel('velocidade-u')
plt.show()
