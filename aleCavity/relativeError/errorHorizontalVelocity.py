# =======================
# Importing the libraries
# =======================

import sys

import numpy as np
from tqdm import tqdm
from time import time
import matplotlib.pyplot as plt
import tikzplotlib

print( '------------' )
print( 'COMPARATION:' )
print( '------------' )


# ------------
# current work
# ------------

# ---------------------------------------------------
#mesh1
y_c = np.zeros([17,1], dtype = float)
u_c = np.zeros([17,1], dtype = float)

y_c[16] = 1.0000
y_c[15] = 0.9766
y_c[14] = 0.9688
y_c[13] = 0.9609
y_c[12] = 0.9531
y_c[11] = 0.8516
y_c[10] = 0.7344
y_c[9] = 0.6172
y_c[8] = 0.5000
y_c[7] = 0.4531
y_c[6] = 0.2813
y_c[5] = 0.1719
y_c[4] = 0.1016
y_c[3] = 0.0703
y_c[2] = 0.0625
y_c[1] = 0.0547
y_c[0] = 0.0000

u_c[16] =  1.00000
u_c[15] =  0.876149
u_c[14] =  0.833071
u_c[13] =  0.789992
u_c[12] =  0.746913
u_c[11] =  0.265792
u_c[10] =  -0.05403
u_c[9]  =  -0.18861
u_c[8]  =  -0.20548
u_c[7]  =  -0.19161
u_c[6]  =  -0.13111
u_c[5]  =  -0.07682
u_c[4]  =  -0.05030
u_c[3]  =  -0.03481
u_c[2]  =  -0.00313
u_c[1]  =  -0.00273
u_c[0]  =   0.00000
# ---------------------------------------------------


# ---------------------------------------------------
#mesh2
y_d = np.zeros([17,1], dtype = float)
u_d = np.zeros([17,1], dtype = float)

y_d[16] = 1.0000
y_d[15] = 0.9766
y_d[14] = 0.9688
y_d[13] = 0.9609
y_d[12] = 0.9531
y_d[11] = 0.8516
y_d[10] = 0.7344
y_d[9] = 0.6172
y_d[8] = 0.5000
y_d[7] = 0.4531
y_d[6] = 0.2813
y_d[5] = 0.1719
y_d[4] = 0.1016
y_d[3] = 0.0703
y_d[2] = 0.0625
y_d[1] = 0.0547
y_d[0] = 0.0000

u_d[16] =   1.00000
u_d[15] =  0.861118
u_d[14] =  0.82061
u_d[13] =  0.768529
u_d[12] =  0.72823
u_d[11] =  0.235676
u_d[10] =  -0.087368
u_d[9]  =  -0.197612
u_d[8]  =  -0.196846
u_d[7]  =  -0.182946
u_d[6]  =  -0.11352
u_d[5]  =  -0.072540
u_d[4]  =  -0.045877
u_d[3]  =  -0.032930
u_d[2]  =  -0.030078
u_d[1]  =  -0.02682
u_d[0]  =   0.00000
# ---------------------------------------------------


# ---------------------------------------------------
#mesh3
y_e = np.zeros([17,1], dtype = float)
u_e = np.zeros([17,1], dtype = float)

y_e[16] = 1.0000
y_e[15] = 0.9766
y_e[14] = 0.9688
y_e[13] = 0.9609
y_e[12] = 0.9531
y_e[11] = 0.8516
y_e[10] = 0.7344
y_e[9] = 0.6172
y_e[8] = 0.5000
y_e[7] = 0.4531
y_e[6] = 0.2813
y_e[5] = 0.1719
y_e[4] = 0.1016
y_e[3] = 0.0703
y_e[2] = 0.0625
y_e[1] = 0.0547
y_e[0] = 0.0000

u_e[16] =   1.00000
u_e[15] =  0.855972
u_e[14] =  0.814606
u_e[13] =  0.767267
u_e[12] =  0.719725
u_e[11] =  0.222285
u_e[10] =  -0.10305
u_e[9]  =  -0.202432
u_e[8]  =  -0.182000
u_e[7]  =  -0.169795
u_e[6]  =  -0.098054
u_e[5]  =  -0.065653
u_e[4]  =  -0.042567
u_e[3]  =  -0.013112
u_e[2]  =  -0.028301
u_e[1]  =  -0.025058
u_e[0]  =   0.00000
# ---------------------------------------------------


# ---------------------------------------------------
#mesh4
y_f = np.zeros([17,1], dtype = float)
u_f = np.zeros([17,1], dtype = float)

y_f[16] = 1.0000
y_f[15] = 0.9766
y_f[14] = 0.9688
y_f[13] = 0.9609
y_f[12] = 0.9531
y_f[11] = 0.8516
y_f[10] = 0.7344
y_f[9] = 0.6172
y_f[8] = 0.5000
y_f[7] = 0.4531
y_f[6] = 0.2813
y_f[5] = 0.1719
y_f[4] = 0.1016
y_f[3] = 0.0703
y_f[2] = 0.0625
y_f[1] = 0.0547
y_f[0] = 0.0000

u_f[16] =   1.00000
u_f[15] =  0.934821
u_f[14] =  0.879428
u_f[13] =  0.827573
u_f[12] =  0.780926
u_f[11] =  0.35342
u_f[10] =  0.035324
u_f[9]  =  -0.169402
u_f[8]  =  -0.256354
u_f[7]  =  -0.262722
u_f[6]  =  -0.203894
u_f[5]  =  -0.138579
u_f[4]  =  -0.088170
u_f[3]  =  -0.062264
u_f[2]  =  -0.055455
u_f[1]  =  -0.050008
u_f[0]  =   0.00000
# ---------------------------------------------------

# ---------------------------------------------------
#mesh5
y_g = np.zeros([17,1], dtype = float)
u_g = np.zeros([17,1], dtype = float)

y_g[16] = 1.0000
y_g[15] = 0.9766
y_g[14] = 0.9688
y_g[13] = 0.9609
y_g[12] = 0.9531
y_g[11] = 0.8516
y_g[10] = 0.7344
y_g[9] = 0.6172
y_g[8] = 0.5000
y_g[7] = 0.4531
y_g[6] = 0.2813
y_g[5] = 0.1719
y_g[4] = 0.1016
y_g[3] = 0.0703
y_g[2] = 0.0625
y_g[1] = 0.0547
y_g[0] = 0.0000

u_g[16] =  1.0000
u_g[15] =  0.87345
u_g[14] =  0.83307
u_g[13] =  0.78999
u_g[12] =  0.74691
u_g[11] =  0.26752
u_g[10] =  -0.0550
u_g[9]  =  -0.1886
u_g[8]  =  -0.2054
u_g[7]  =  -0.1916
u_g[6]  =  -0.1315
u_g[5]  =  -0.0791
u_g[4]  =  -0.0498
u_g[3]  =  -0.0348
u_g[2]  =  -0.0308
u_g[1]  =  -0.0283
u_g[0]  =  0.0000
# ---------------------------------------------------










# -----------
# GHIA et al.
# -----------

y_a = np.zeros([17,1], dtype = float)
u_a = np.zeros([17,1], dtype = float)


y_a[16] = 1.0000
y_a[15] = 0.9766
y_a[14] = 0.9688
y_a[13] = 0.9609
y_a[12] = 0.9531
y_a[11] = 0.8516
y_a[10] = 0.7344
y_a[9] = 0.6172
y_a[8] = 0.5000
y_a[7] = 0.4531
y_a[6] = 0.2813
y_a[5] = 0.1719
y_a[4] = 0.1016
y_a[3] = 0.0703
y_a[2] = 0.0625
y_a[1] = 0.0547
y_a[0] = 0.0000

u_a[16] = 1.00000
u_a[15] = 0.84123 
u_a[14] = 0.78871 
u_a[13] = 0.73722 
u_a[12] = 0.68717 
u_a[11] = 0.23151 
u_a[10] = 0.00332 
u_a[9] = -0.13641 
u_a[8] = -0.20581 
u_a[7] = -0.21090 
u_a[6] = -0.15662 
u_a[5] = -0.10150 
u_a[4] = -0.06434 
u_a[3] = -0.04775 
u_a[2] = -0.04192 
u_a[1] = -0.03717 
u_a[0] = 0.00000




# -------------
# MARCHI et al.
# -------------

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
# plot profile
cav_num = []
with open('mesh1HorizontalVelocity.csv') as cav:
 for line in cav:
  row = line.split(',')
  cav_num.append(row[:])

y1 = np.zeros([len(cav_num)-1,1], dtype = float)
vx1 = np.zeros([len(cav_num)-1,1], dtype = float)
for i in range(1,len(cav_num)):
 vx1[i-1] = cav_num[i][1]
 y1[i-1] = cav_num[i][7]
# ---------------------------------------------------



# ---------------------------------------------------
#Error mesh1
numError = np.zeros([len(y_a),1], dtype = float)
demError = np.zeros([len(y_a),1], dtype = float)
for i in range(0,len(y_a)-1):
 if not u_a[i] == 0:
  numError[i] = (u_c[i] - u_a[i])**2
  demError[i] = (u_a[i])**2

num = np.sum(numError)
dem = np.sum(demError)
avgError_mesh1 = np.sqrt(num/dem)*100.0

print( "Relative Error for mesh1 is:" ) 
print (avgError_mesh1)
# ---------------------------------------------------


# ---------------------------------------------------
#Error mesh2
numError = np.zeros([len(y_a),1], dtype = float)
demError = np.zeros([len(y_a),1], dtype = float)
for i in range(0,len(y_a)-1):
 if not u_a[i] == 0:
  numError[i] = (u_d[i] - u_a[i])**2
  demError[i] = (u_a[i])**2

num = np.sum(numError)
dem = np.sum(demError)
avgError_mesh2 = np.sqrt(num/dem)*100.0

print( "Relative Error for mesh2 is:" ) 
print (avgError_mesh2)
# ---------------------------------------------------


# ---------------------------------------------------
#Error mesh3
numError = np.zeros([len(y_a),1], dtype = float)
demError = np.zeros([len(y_a),1], dtype = float)
for i in range(0,len(y_a)-1):
 if not u_a[i] == 0:
  numError[i] = (u_e[i] - u_a[i])**2
  demError[i] = (u_a[i])**2

num = np.sum(numError)
dem = np.sum(demError)
avgError_mesh3 = np.sqrt(num/dem)*100.0

print( "Relative Error for mesh3 is:" ) 
print (avgError_mesh3)
# ---------------------------------------------------


# ---------------------------------------------------
#Error mesh4
numError = np.zeros([len(y_a),1], dtype = float)
demError = np.zeros([len(y_a),1], dtype = float)
for i in range(0,len(y_a)-1):
 if not u_a[i] == 0:
  numError[i] = (u_f[i] - u_a[i])**2
  demError[i] = (u_a[i])**2

num = np.sum(numError)
dem = np.sum(demError)
avgError_mesh4 = np.sqrt(num/dem)*100.0

print( "Relative Error for mesh4 is:" ) 
print (avgError_mesh4)
# ---------------------------------------------------


# ---------------------------------------------------
#Error mesh5
numError = np.zeros([len(y_a),1], dtype = float)
demError = np.zeros([len(y_a),1], dtype = float)
for i in range(0,len(y_a)-1):
 if not u_a[i] == 0:
  numError[i] = (u_g[i] - u_a[i])**2
  demError[i] = (u_a[i])**2

num = np.sum(numError)
dem = np.sum(demError)
avgError_mesh5 = np.sqrt(num/dem)*100.0

print( "Relative Error for mesh5 is:" ) 
print( avgError_mesh5)
# ---------------------------------------------------



plt.plot(vx1, y1, '-', color='black', label = "Horizontal Velocity Profile")
plt.plot(u_a, y_a, 'o', color='black', label = "Ghia et al. (1982)")
plt.plot(u_c, y_c, 'x', color='black', label = "current work")
plt.xlabel("Horizontal Velocity")
plt.ylabel("Y")
plt.legend(loc = 4)
tikzplotlib.save("teste.tex")
plt.show()

