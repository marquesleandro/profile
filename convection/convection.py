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
with open('convection_exact10.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

ye0 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe0 = np.zeros([len(cav_num)-1,1], dtype = float)
ye1 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe1 = np.zeros([len(cav_num)-1,1], dtype = float)
ye2 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe2 = np.zeros([len(cav_num)-1,1], dtype = float)
ye3 = np.zeros([len(cav_num)-1,1], dtype = float)
vxe3 = np.zeros([len(cav_num)-1,1], dtype = float)

for i in range(1,len(cav_num)):
 vxe0[i-1] = cav_num[i][3]
 vxe1[i-1] = cav_num[i][4]
 vxe2[i-1] = cav_num[i][5]
 vxe3[i-1] = cav_num[i][6]
 ye0[i-1] = cav_num[i][7]




end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""

plt.plot(y1, vx1, '--', color='black', label = "Galerkin")
plt.plot(y2, vx2, '-', color='black', label = "Taylor-Galerkin")
plt.plot(ye0, vxe0, '--', color='black', label = "solucao analitica")
plt.plot(ye0, vxe1, '--', color='black', label = "solucao analitica")
plt.plot(ye0, vxe2, '--', color='black', label = "solucao analitica")
plt.plot(ye0, vxe3, '--', color='black', label = "solucao analitica")
plt.legend(loc = 1)
plt.ylabel('escalar c')
plt.xlabel('posicao')
plt.show()
