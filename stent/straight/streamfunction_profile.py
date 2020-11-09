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
with open('stream1.csv') as cav:
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
 vx1[i] = cav_num[i*aa][4]
 y1[i] = cav_num[i*aa][7]

#vx1[0] = 2.709
#vx1[nn-1] = 2.709
#y1[0] = 1.0
#y1[nn-1] = 0.0



# -----
# 1.0 s
# -----

cav_num = []
with open('stream2.csv') as cav:
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
 vx2[i] = cav_num[i*aa][4]
 y2[i] = cav_num[i*aa][7]




# -----
# 3.0 s
# -----

cav_num = []
with open('stream3.csv') as cav:
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
 vx3[i] = cav_num[i*aa][4]
 y3[i] = cav_num[i*aa][7]



# -----
# 10.0 s
# -----

cav_num = []
with open('stream4.csv') as cav:
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
 vx4[i] = cav_num[i*aa][4]
 y4[i] = cav_num[i*aa][7]

vx4[nn-1] = 1.0
y4[nn-1] = 1.0

# -----
# exact
# -----
vxe = np.zeros([50,1], dtype = float)
ye = np.zeros([50,1], dtype = float)

u_max = 1.5
L = 1.0
for i in range(0,50):
 ye[i] = (i/50.0)
 vxe[i] = (u_max*ye[i]/(L**2)) - ((u_max*(ye[i]**3))/(3*(L**2)))

print len(y4)
print len(ye)
print len(y4)/len(ye)
factor = len(y4)/len(ye)

erro = []
for i in range(0,len(y4)-1):
 err = np.sqrt((vxe[i/factor] - vx4[i])**2)
 erro.append(err)

avg_erro = sum(erro)/len(erro)

print avg_erro






end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""




plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='fourier')
ax = plt.axes()
ax.set_xlabel(r'Streamfunction Field',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('auto')
plt.plot(vx1, y1, '1', color='black', label = "t = 0.5s")
plt.plot(vx3, y3, '.', color='black', label = "t = 1.0s")
plt.plot(vx4, y4, '--', color='black', label = "t = 100.0s")
plt.plot(vxe, ye, '-', color='black', label = "analytical solution")
plt.legend(loc = 4)
plt.show()
