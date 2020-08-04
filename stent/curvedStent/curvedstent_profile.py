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
with open('vel05.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y1 = np.zeros([len(cav_num)-1,1], dtype = float)
#vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
#for i in range(1,len(cav_num)):
# vx1[i-1] = cav_num[i][1]
# y1[i-1] = cav_num[i][7]


nn = 50
y1 = np.zeros([nn,1], dtype = float)
vx1 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx1[i] = cav_num[i*aa][1]
 y1[i] = cav_num[i*aa][7]

vx1[0] = 2.89
vx1[nn-1] = 2.89
y1[0] = 1.0
y1[nn-1] = 0.0



# -----
# 1.0 s
# -----

cav_num = []
with open('vel1.csv') as cav:
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
with open('vel5.csv') as cav:
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
with open('vel100.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num),1], dtype = float)
vx4 = np.zeros([len(cav_num),1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]

y4[len(cav_num)-1] = 1.0
vx4[len(cav_num)-1] = 0.0


end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""

for i in range(0,len(y1)):
 if y1[i] > 0.5:
  y1[i] = 0.0

for i in range(0,len(y2)):
 if y2[i] > 0.5:
  y2[i] = 0.0

for i in range(0,len(y3)):
 if y3[i] > 0.5:
  y3[i] = 0.0

for i in range(0,len(y4)):
 if y4[i] > 0.5:
  y4[i] = 0.0




plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'Horizontal Velocity',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('auto')
plt.plot(vx1, y1, '.', color='black', label = "t = 0.5s")
plt.plot(vx2, y2, '--', color='black', fillstyle='none', label = "t = 1.0s")
#plt.plot(vx3, y3, '--', color='black', label = "t = 5.0s")
plt.plot(vx4, y4, '-', color='black', label = "t=100.0s")
plt.legend(loc = 3)
plt.show()
