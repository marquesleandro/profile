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

# -----
# 0.1 s
# -----

cav_num = []
with open('real_200.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][1]
 y1[i-1] = cav_num[i][7]

# -----
# 1.0 s
# -----

cav_num = []
with open('real_2000.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][1]
 y2[i-1] = cav_num[i][7]


# -----
# 3.0 s
# -----

cav_num = []
with open('real_6000.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]



# -----
# 10.0 s
# -----

cav_num = []
with open('real_20000.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num),1], dtype = float)
vx4 = np.zeros([len(cav_num),1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]

y4[len(cav_num)-1] = 0.7
vx4[len(cav_num)-1] = 0.0


plt.xticks(np.arange(0.0, 3.5, 0.25))
plt.yticks(np.arange(0.0, 1.1, 0.1))
plt.plot(vx1, y1, '2', color='black', label = "t = 0.1")
plt.plot(vx2, y2, '.', color='black', fillstyle='none', label = "t = 1.0")
plt.plot(vx3, y3, '--', color='black', label = "t = 3.0")
plt.plot(vx4, y4, '-', color='black', label = "t = 10.0")
plt.legend(loc = 3)
plt.ylabel('y')
plt.xlabel('velocity-u')
plt.show()
