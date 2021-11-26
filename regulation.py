# -*- coding: utf-8 -*-
"""Regulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yx_Kzdo_IjNzZXqaYdtVsAnxzjCwJusU
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
np.set_printoptions(threshold=sys.maxsize)
N = 101
dt = 0.01
L = float(0.05)
timesteps = round(10/dt)
dx = L/(N-1)
q = 1
k = 73
t = 1000
rhocp = 31.79*10**4
alpha = 2.3*10**-4
r = alpha*dt/dx**2
A = np.zeros((N, N))
B = np.zeros((N, N))
for i in range(N):
    if i == 0:
        A[i, :] = [1+2*r if j == 0 else -(2*r) if j == 1 else 0 for j in range(N)]
    elif i == N-1:
        A[i, :] = [-(2*r) if j == N-2 else (1+2*r) if j == N-1 else 0 for j in range(N)]
    else:
        A[i, :] = [-r if j == i-1 or j == i+1 else 1+2*r if j == i else 0 for j in range(N)]
x = np.linspace(0, 5, N)
T0 = np.asarray([293 for j in range(N)])
Tn = T0

P = np.zeros(t+1)


i = 0
for j in range(timesteps+1):
  Tn[0] = Tn[0] + q*2*dt/(rhocp*dx)    
  T = np.linalg.solve(A,Tn)
  Tn = T
  if j % round((timesteps/(t))) == 0:
    j=j*dt
    P[i] = T[-1]
    i += 1


# i = np.size(P)
# S=0
# for j in range(i-1):
#   # print(P[j])
#   S += P[j]
# print(S)
# S = S/i
# M = np.zeros(i)
# print(S)
# M1 = 0
# for j in range(i-1):
#   M[j] = P[j] - S
#   # print(M)
#   M = np.square(M)
#   # print(M)
#   M1 += M[j]



mean = 0
SD = 0.01
x = np.random.normal(mean,SD,t+1)
plt.figure(2)
count , bins , patches = plt.hist(x,50,density = True)
plt.plot(bins, 1/(SD * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * SD**2) ), linewidth=2, color='r')
plt.show()
# plt.savefig("Project2.jpg")


U = np.linspace(0 , t , t+1)
W = P - x
plt.figure(figsize=(10,10))
plt.plot(U, W, linewidth=4, label='Sensor Temperature' )
plt.plot(U, P, linewidth=2, label='Real Temperature' )
plt.xlabel("Number of read temperature")        
plt.ylabel('Temperature [K]')
plt.title('Temperature at x=L')
plt.legend()
plt.grid()


# Firstdomain = 0    #firstdomain : +-sigma
# # print(x)
# for j in range(t+1) :
#   if x[j] <= SD and x[j] >= -SD :
#     Firstdomain += 1
# print(Firstdomain)


# Seconddomain = 0      #Seconddomain : +-2*sigma
# for j in range(t+1) :
#   if x[j] <= 2*SD and x[j] >= -2*SD :
#     Seconddomain += 1
# print(Seconddomain)

Phis = np.zeros(100)

for i in range(100):
  Phis[i] = P[i*10] - 293







q = np.zeros(101)
i = 0
Sum1=0
Sum2 = 0
Sumphi = 0
T1 = np.asarray([293 for j in range(100)])
for r in range(1,11):
  for n in range(1,r):
    Sum = Phis[r-1]**2
    SumPhi += Sum


 
  for j in range(timesteps+1):
    
      for m in range(r):
        Sum1 += (P[i+r-1]-T1[i+r]) * Phis[i+r-1]
        Sum2 += Sum1
  for g in range(101):
    Q = (Sum2)/ Sumphi
    q = Q
    Tn[0] = Tn[0] + q*2*dt/(rhocp*dx)    
    T = np.linalg.solve(A,Tn)
    Tn = T
    if j % round((timesteps/(t))) == 0:
      j=j*dt
      T1[i] = T[-1]
      i += 1

import numpy as np
a = np.zeros(10) 
b = (a +1)*  2 +5
print(b)