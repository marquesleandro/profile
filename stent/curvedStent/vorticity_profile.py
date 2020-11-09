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
with open('vorticity1.csv') as cav:
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
 vx1[i] = cav_num[i*aa][0]
 y1[i] = cav_num[i*aa][7]

#vx1[0] = 2.709
#vx1[nn-1] = 2.709
#y1[0] = 1.0
#y1[nn-1] = 0.0



# -----
# 1.0 s
# -----

cav_num = []
with open('vorticity2.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y2 = np.zeros([len(cav_num)-1,1], dtype = float)
#vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
#for i in range(1,len(cav_num)):
# vx2[i-1] = cav_num[i][7]
# y2[i-1] = cav_num[i][16]

nn = 50
y2 = np.zeros([nn,1], dtype = float)
vx2 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx2[i] = cav_num[i*aa][0]
 y2[i] = cav_num[i*aa][7]




# -----
# 3.0 s
# -----

cav_num = []
with open('vorticity3.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y3 = np.zeros([len(cav_num)-1,1], dtype = float)
#vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
#for i in range(1,len(cav_num)):
# vx3[i-1] = cav_num[i][7]
# y3[i-1] = cav_num[i][16]


nn = 50
y3 = np.zeros([nn,1], dtype = float)
vx3 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx3[i] = cav_num[i*aa][0]
 y3[i] = cav_num[i*aa][7]



# -----
# 10.0 s
# -----

cav_num = []
with open('vorticity4.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

#y4 = np.zeros([len(cav_num),1], dtype = float)
#vx4 = np.zeros([len(cav_num),1], dtype = float)
#for i in range(1,len(cav_num)):
# vx4[i-1] = cav_num[i][7]
# y4[i-1] = cav_num[i][16]


nn = 50
y4 = np.zeros([nn,1], dtype = float)
vx4 = np.zeros([nn,1], dtype = float)
for i in range(1,nn-1):
 aa = int(len(cav_num)/nn)
 vx4[i] = cav_num[i*aa][0]
 y4[i] = cav_num[i*aa][7]



end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""




plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'Vorticity Field',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('auto')
#plt.plot(vx1, y1, '1', color='black', label = "t = 0.5s")
plt.plot(vx2, y2, '.', color='black', label = "t = 0.5s")
plt.plot(vx3, y3, '--', color='black', label = "t = 1.0s")
plt.plot(vx4, y4, '-', color='black', label = "t = 100.0s")
plt.legend(loc = 4)
plt.show()
