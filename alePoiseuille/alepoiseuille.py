# =======================
# Importing the libraries
# =======================

import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt
import tikzplotlib

'''
cav_num = []
with open('poiseulle_20h.csv') as cav:
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
with open('poiseulle_40h.csv') as cav:
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
with open('poiseulle_200h.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]
'''

# ------------
# Steady State
# ------------

cav_num = []
with open('alepoiseuille.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]

print (len(cav_num))
node = 25
vxn = np.zeros([node+1,1], dtype = float)
yn = np.zeros([node+1,1], dtype = float)
for i in range(0,node+1):
 print (i*int(len(cav_num)/node))
 vxn[i] = vx4[i*int(len(cav_num)/node)]
 yn[i] = y4[i*int(len(cav_num)/node)]



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





plt.clf()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = plt.axes()
ax.set_xlabel(r'Horizontal Velocity',fontsize=14)
ax.set_ylabel(r'y',fontsize=14)
ax.set_aspect('equal')
#plt.plot(vx1, y1, '2', color='black', label = "t = 0.1")
#plt.plot(vx3, y3, '.', color='black', fillstyle='none', label = "t = 1.0")
plt.plot(vxn, yn, 's', color='black', label = "numerical solution")
plt.plot(vxe, ye, '--', color='black', label = "analytical solution")
plt.legend(loc = 3)
tikzplotlib.save("horizontalVelocity.tex")
plt.show()

