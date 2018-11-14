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
# Galerkin
# -----

cav_num = []
with open('convection_galerkin_950.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][4]
 y1[i-1] = cav_num[i][6]

# -----
# Taylor-Galerkin
# -----

cav_num = []
with open('convection_taylor_950.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][4]
 y2[i-1] = cav_num[i][6]


# -----
# Exata
# -----

cav_num = []
with open('convection_exact.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][4]
 y3[i-1] = cav_num[i][6]

end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""

plt.plot(y1, vx1, '--', color='black', label = "Galerkin")
plt.plot(y2, vx2, '-', color='black', label = "Taylor-Galerkin")
#plt.plot(y3, vx3, '--', color='black', label = "solucao analitica")
plt.legend(loc = 1)
plt.ylabel('escalar c')
plt.xlabel('posicao')
plt.show()
