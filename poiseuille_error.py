# =======================
# Importing the libraries
# =======================

import sys

import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt

print '------------'
print 'COMPARATION:'
print '------------'

start_time = time()

# -----
# malha 2
# -----

cav_num = []
with open('poiseuille_erro2.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx2[i-1] = cav_num[i][1]
 y2[i-1] = cav_num[i][7]

# -----
# malha 3
# -----

cav_num = []
with open('poiseuille_erro3.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx3[i-1] = cav_num[i][1]
 y3[i-1] = cav_num[i][7]


# -----
# malha 4
# -----

cav_num = []
with open('poiseuille_erro4.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx4[i-1] = cav_num[i][1]
 y4[i-1] = cav_num[i][7]

# -----
# malha 5
# -----

cav_num = []
with open('poiseuille_erro5.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y5 = np.zeros([len(cav_num)-1,1], dtype = float)
vx5 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx5[i-1] = cav_num[i][1]
 y5[i-1] = cav_num[i][7]



# -----
# malha 6
# -----

cav_num = []
with open('poiseuille_erro6.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y6 = np.zeros([len(cav_num)-1,1], dtype = float)
vx6 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx6[i-1] = cav_num[i][1]
 y6[i-1] = cav_num[i][7]



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

# -----
# error
# -----

malha = len(vx4)
vel = vx4
y = y4

err1 = np.zeros([malha,1], dtype = float)
err2 = np.zeros([malha,1], dtype = float)
vx_a = np.zeros([malha,1], dtype = float)

# erro malha 2
for i in range(0,len(vx2)):
 if not vx2[i] == 0:
  h = y2[i]
  vx_a[i] = ((4.0*u_max*h)/L**2)*(L - h)
  err1[i] = (vx2[i] - vx_a[i])**2
  err2[i] = vx_a[i]**2
 
num = np.sum(err1)
den = np.sum(err2)
error2 = np.sqrt(num/den)

# erro malha 3
for i in range(0,len(vx3)):
 if not vx3[i] == 0:
  h = y3[i]
  vx_a[i] = ((4.0*u_max*h)/L**2)*(L - h)
  err1[i] = (vx3[i] - vx_a[i])**2
  err2[i] = vx_a[i]**2
 
num = np.sum(err1)
den = np.sum(err2)
error3 = np.sqrt(num/den)

# erro malha 4
for i in range(0,len(vx4)):
 if not vx4[i] == 0:
  h = y4[i]
  vx_a[i] = ((4.0*u_max*h)/L**2)*(L - h)
  err1[i] = (vx4[i] - vx_a[i])**2
  err2[i] = vx_a[i]**2
 
num = np.sum(err1)
den = np.sum(err2)
error4 = np.sqrt(num/den)

# erro malha 5
for i in range(0,len(vx5)):
 if not vx5[i] == 0:
  h = y5[i]
  vx_a[i] = ((4.0*u_max*h)/L**2)*(L - h)
  err1[i] = (vx5[i] - vx_a[i])**2
  err2[i] = vx_a[i]**2
 
num = np.sum(err1)
den = np.sum(err2)
error5 = np.sqrt(num/den)


# erro malha 6
for i in range(0,len(vx6)):
 if not vx6[i] == 0:
  h = y6[i]
  vx_a[i] = ((4.0*u_max*h)/L**2)*(L - h)
  err1[i] = (vx6[i] - vx_a[i])**2
  err2[i] = vx_a[i]**2
 
num = np.sum(err1)
den = np.sum(err2)
error6 = np.sqrt(num/den)




elementos = np.zeros([5,1], dtype = int)
error = np.zeros([5,1], dtype = float)

elementos[0] = 100
elementos[1] = 400
elementos[2] = 1600
elementos[3] = 6400
elementos[4] = 25600

error[0] = error2
error[1] = error3
error[2] = error4
error[3] = error5
error[4] = error6

error1 = error*20

print error

end_time = time()
print 'time duration: %.1f seconds' %(end_time - start_time)
print ""

elementos1 = np.zeros([5,1], dtype = int)
elementos1[4] = 100
elementos1[3] = 400
elementos1[2] = 1600
elementos1[1] = 6400
elementos1[0] = 25600

elementos1 = elementos1*0.001

plt.loglog(elementos,error, '-s', color = 'black', label = 'numerical solution')
plt.loglog(elementos,elementos1, ':', color = 'black', label = 'first order')
plt.loglog(elementos,elementos1**2, '-.', color = 'black', label = 'second order')
plt.legend(loc = 1)
plt.ylabel('relative error')
plt.xlabel('elements numbers\n\n(b)')
plt.show()
