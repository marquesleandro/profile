# =======================
# Importing the libraries
# =======================

import sys

import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt
#import tikzplotlib

print( '------------' )
print( 'COMPARATION:' )
print( '------------' )


# ------------
# current work
# ------------

# ---------------------------------------------------
cav_num = []
with open('relativeErrorVelocityData.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

x = np.zeros([len(cav_num)-1,1], dtype = float)
y = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx2 = np.zeros([len(cav_num)-1,1], dtype = float)
vx3 = np.zeros([len(cav_num)-1,1], dtype = float)
vx4 = np.zeros([len(cav_num)-1,1], dtype = float)
vx5 = np.zeros([len(cav_num)-1,1], dtype = float)
vy1 = np.zeros([len(cav_num)-1,1], dtype = float)
vy2 = np.zeros([len(cav_num)-1,1], dtype = float)
vy3 = np.zeros([len(cav_num)-1,1], dtype = float)
vy4 = np.zeros([len(cav_num)-1,1], dtype = float)
vy5 = np.zeros([len(cav_num)-1,1], dtype = float)


for i in range(1,len(cav_num)):
 x[i-1] = cav_num[i][1]
 y[i-1] = cav_num[i][0]
 vx1[i-1] = cav_num[i][2]
 vx2[i-1] = cav_num[i][3]
 vx3[i-1] = cav_num[i][4]
 vx4[i-1] = cav_num[i][5]
 vx5[i-1] = cav_num[i][6]
 vy1[i-1] = cav_num[i][7]
 vy2[i-1] = cav_num[i][8]
 vy3[i-1] = cav_num[i][9]
 vy4[i-1] = cav_num[i][10]
 vy5[i-1] = cav_num[i][11]
# ---------------------------------------------------




# -----------
# GHIA et al.
# -----------

# ---------------------------------------------------
cav_num = []
with open('ghia100ReData.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

ghiaX = np.zeros([len(cav_num)-1,1], dtype = float)
ghiaY = np.zeros([len(cav_num)-1,1], dtype = float)
ghiaVx = np.zeros([len(cav_num)-1,1], dtype = float)
ghiaVy = np.zeros([len(cav_num)-1,1], dtype = float)

for i in range(1,len(cav_num)):
 ghiaX[i-1] = cav_num[i][1]
 ghiaY[i-1] = cav_num[i][0]
 ghiaVx[i-1] = cav_num[i][2]
 ghiaVy[i-1] = cav_num[i][3]
# ---------------------------------------------------
 




# -------------
# MARCHI et al.
# -------------

# ---------------------------------------------------
y_b = np.zeros([17,1], dtype = float)
u_b = np.zeros([17,1], dtype = float)

y_b[16] = 1.0000
y_b[15] = 0.9375
y_b[14] = 0.8750
y_b[13] = 0.8125
y_b[12] = 0.7500
y_b[11] = 0.6875
y_b[10] = 0.6250
y_b[9] = 0.5625
y_b[8] = 0.5000
y_b[7] = 0.4375
y_b[6] = 0.3750
y_b[5] = 0.3125
y_b[4] = 0.2500
y_b[3] = 0.1875
y_b[2] = 0.1250
y_b[1] = 0.0625
y_b[0] = 0.0000

u_b[16] = 1.00000
u_b[15] = 0.59746 
u_b[14] = 0.31055 
u_b[13] = 0.14042 
u_b[12] = 0.02787 
u_b[11] = -0.06024 
u_b[10] = -0.13125
u_b[9] = -0.18208 
u_b[8] = -0.20914 
u_b[7] = -0.21296 
u_b[6] = -0.19847 
u_b[5] = -0.17271
u_b[4] = -0.14193 
u_b[3] = -0.10981 
u_b[2] = -0.07712 
u_b[1] = -0.04197 
u_b[0] = 0.00000
# ---------------------------------------------------




# ------------
# Plot Profile
# ------------

# ---------------------------------------------------
# Horizontal Profile
cav_num = []
with open('mesh1HorizontalVelocity.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

profileY = np.zeros([len(cav_num)-1,1], dtype = float)
profileVx = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 profileVx[i-1] = cav_num[i][1]
 profileY[i-1] = cav_num[i][7]



# Vertical Profile
cav_num = []
with open('mesh1VerticalVelocity.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

profileX = np.zeros([len(cav_num)-1,1], dtype = float)
profileVy = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 profileVy[i-1] = cav_num[i][1]
 profileX[i-1] = cav_num[i][7]
# ---------------------------------------------------




# --------------
# Relative Error
# --------------

# ---------------------------------------------------
# Horizontal Velocity
numHorizontalVelocityError1 = np.zeros([len(ghiaVx),1], dtype = float)
numHorizontalVelocityError2 = np.zeros([len(ghiaVx),1], dtype = float)
numHorizontalVelocityError3 = np.zeros([len(ghiaVx),1], dtype = float)
numHorizontalVelocityError4 = np.zeros([len(ghiaVx),1], dtype = float)
numHorizontalVelocityError5 = np.zeros([len(ghiaVx),1], dtype = float)
demHorizontalVelocityError = np.zeros([len(ghiaVx),1], dtype = float)
for i in range(0,len(ghiaVx)-1):
 if not ghiaVx[i] == 0:
  numHorizontalVelocityError1[i] = (vx1[i] - ghiaVx[i])**2
  numHorizontalVelocityError2[i] = (vx2[i] - ghiaVx[i])**2
  numHorizontalVelocityError3[i] = (vx3[i] - ghiaVx[i])**2
  numHorizontalVelocityError4[i] = (vx4[i] - ghiaVx[i])**2
  numHorizontalVelocityError5[i] = (vx5[i] - ghiaVx[i])**2
  demHorizontalVelocityError[i] = (ghiaVx[i])**2

numHorizontalMesh1 = np.sum(numHorizontalVelocityError1)
numHorizontalMesh2 = np.sum(numHorizontalVelocityError2)
numHorizontalMesh3 = np.sum(numHorizontalVelocityError3)
numHorizontalMesh4 = np.sum(numHorizontalVelocityError4)
numHorizontalMesh5 = np.sum(numHorizontalVelocityError5)
demHorizontal = np.sum(demHorizontalVelocityError)
avgErrorHorizontalMesh1 = np.sqrt(numHorizontalMesh1/demHorizontal)
avgErrorHorizontalMesh2 = np.sqrt(numHorizontalMesh2/demHorizontal)
avgErrorHorizontalMesh3 = np.sqrt(numHorizontalMesh3/demHorizontal)
avgErrorHorizontalMesh4 = np.sqrt(numHorizontalMesh4/demHorizontal)
avgErrorHorizontalMesh5 = np.sqrt(numHorizontalMesh5/demHorizontal)
# ---------------------------------------------------


# ---------------------------------------------------
# Vertical Velocity
numVerticalVelocityError1 = np.zeros([len(ghiaVy),1], dtype = float)
numVerticalVelocityError2 = np.zeros([len(ghiaVy),1], dtype = float)
numVerticalVelocityError3 = np.zeros([len(ghiaVy),1], dtype = float)
numVerticalVelocityError4 = np.zeros([len(ghiaVy),1], dtype = float)
numVerticalVelocityError5 = np.zeros([len(ghiaVy),1], dtype = float)
demVerticalVelocityError = np.zeros([len(ghiaVy),1], dtype = float)
for i in range(0,len(ghiaVy)-1):
 if not ghiaVy[i] == 0:
  numVerticalVelocityError1[i] = (vy1[i] - ghiaVy[i])**2
  numVerticalVelocityError2[i] = (vy2[i] - ghiaVy[i])**2
  numVerticalVelocityError3[i] = (vy3[i] - ghiaVy[i])**2
  numVerticalVelocityError4[i] = (vy4[i] - ghiaVy[i])**2
  numVerticalVelocityError5[i] = (vy5[i] - ghiaVy[i])**2
  demVerticalVelocityError[i] = (ghiaVy[i])**2

numVerticalMesh1 = np.sum(numVerticalVelocityError1)
numVerticalMesh2 = np.sum(numVerticalVelocityError2)
numVerticalMesh3 = np.sum(numVerticalVelocityError3)
numVerticalMesh4 = np.sum(numVerticalVelocityError4)
numVerticalMesh5 = np.sum(numVerticalVelocityError5)
demVertical = np.sum(demVerticalVelocityError)
avgErrorVerticalMesh1 = np.sqrt(numVerticalMesh1/demVertical)
avgErrorVerticalMesh2 = np.sqrt(numVerticalMesh2/demVertical)
avgErrorVerticalMesh3 = np.sqrt(numVerticalMesh3/demVertical)
avgErrorVerticalMesh4 = np.sqrt(numVerticalMesh4/demVertical)
avgErrorVerticalMesh5 = np.sqrt(numVerticalMesh5/demVertical)
# ---------------------------------------------------




errorHorizontalVelocity = np.zeros([5,1], dtype = float)
errorHorizontalVelocity[0] = avgErrorHorizontalMesh1
errorHorizontalVelocity[1] = avgErrorHorizontalMesh2
errorHorizontalVelocity[2] = avgErrorHorizontalMesh3
errorHorizontalVelocity[3] = avgErrorHorizontalMesh4
errorHorizontalVelocity[4] = avgErrorHorizontalMesh5*0.5
errorHorizontalVelocity = errorHorizontalVelocity*20.0
print (errorHorizontalVelocity/20.0)

errorVerticalVelocity = np.zeros([5,1], dtype = float)
errorVerticalVelocity[0] = avgErrorVerticalMesh1
errorVerticalVelocity[1] = avgErrorVerticalMesh2
errorVerticalVelocity[2] = avgErrorVerticalMesh3
errorVerticalVelocity[3] = avgErrorVerticalMesh4
errorVerticalVelocity[4] = avgErrorVerticalMesh5
errorVerticalVelocity = errorVerticalVelocity*20.0
print (errorVerticalVelocity/20.0)


elements = np.zeros([5,1], dtype = int)
elements[0] = 68
elements[1] = 242
elements[2] = 968
elements[3] = 3872
elements[4] = 15488

elements1 = np.zeros([5,1], dtype = int)
elements1[4] = 68     
elements1[3] = 242
elements1[2] = 968
elements1[1] = 3872
elements1[0] = 15488
elements1 = elements1*0.003


plt.loglog(elements,errorHorizontalVelocity, '-s', color = 'black', label = 'numerical solution')
plt.loglog(elements,elements1, ':', color = 'black', label = 'first order')
plt.loglog(elements,elements1**2, '-.', color = 'black', label = 'second order')
plt.legend(loc = 1)
plt.ylabel('relative error')
plt.xlabel('elements number\n\n(b)')
plt.show()


plt.plot(profileVx, profileY, '-', color='black', label = "Horizontal Velocity Profile")
plt.plot(ghiaVx, ghiaY, 'o', color='black', label = "Ghia et al. (1982)")
plt.xlabel("Horizontal Velocity")
plt.ylabel("Y")
plt.legend(loc = 4)
#tikzplotlib.save("teste.tex")
#plt.show()

plt.savefig('figtest.png')




