# Ferran's potato code

import numpy as np
import matplotlib.pyplot as plt

Tf = 180.
T0 = 20.
a = 1.4e-7
rho = 1110
h = 10
k = 40
Lx = 0.4
Nx = 21
dx = Lx/(Nx-1)
Ly = 0.4
Ny = 21
dy = Ly/(Nx-1)
x = np.linspace(0,Lx,Nx)
y = np.linspace(0,Ly,Ny)
dt = 0.1
tend = 20000
T = T0*np.ones((Nx,Ny))
T[10,10] = -15
Tnew = np.copy(T)
t = 0
atx = a*dt/dx**2

iplot = 0

while (t < tend):
	t += dt
	iplot += 1

	# solve first row
	Tnew[0,0] = 2*atx*(T[1,0] + T[0,1] + 2*h*dx/k*Tf) + (1 - 4*atx - 4*a*h*dt/(k*dx))*T[0,0]
	for i in range(1,Nx-1):
		Tnew[i,0] = atx*(2*T[i,1] + T[i-1,0] + T[i+1,0] + 2*h*dx/k*Tf) + (1 - 4*atx - 2*a*h*dt/(k*dx))*T[i,0]
	Tnew[-1,0] = 2*atx*(T[-2,0] + T[-1,1] + 2*h*dx/k*Tf) + (1 - 4*atx - 4*a*h*dt/(k*dx))*T[-1,0]

	# solve for the rows second to last but one
	for j in range(1,Ny-1):
		Tnew[0,j] = atx*(2*T[1,j] + T[0,j+1] + T[0,j-1] + 2*h*dx/k*Tf) + (1 - 4*atx - 2*a*h*dt/(k*dx))*T[0,j]
		for i in range(1,Nx-1):
			Tnew[i,j] = atx*(T[i-1,j] + T[i+1,j] + T[i,j-1] + T[i,j+1]) + (1 - 4*atx)*T[i,j]
		Tnew[-1,j] = atx*(2*T[-2,j] + T[-1,j+1] + T[-1,j-1] + 2*h*dx/k*Tf) + (1 - 4*atx - 2*a*h*dt/(k*dx))*T[-1,j]

	# solve last row
	Tnew[0,-1] = 2*atx*(T[1,-1] + T[-2,-1] + 2*h*dx/k*Tf) + (1 - 4*atx - 4*a*h*dt/(k*dx))*T[0,-1]
	for i in range(1,Nx-1):
		Tnew[i,-1] = atx*(2*T[i,-2] + T[i-1,-1] + T[i+1,-1] + 2*h*dx/k*Tf) + (1 - 4*atx - 2*a*h*dt/(k*dx))*T[i,-1]
	Tnew[-1,-1] = 2*atx*(T[-2,-1] + T[-1,-2] + 2*h*dx/k*Tf) + (1 - 4*atx - 4*a*h*dt/(k*dx))*T[-1,-1]

	T = np.copy(Tnew)

	if (iplot%100 == 0):
		plt.clf()
		plt.pcolor(T)
		#plt.pcolor(T, vmin = -15, vmax = 180)
		plt.colorbar()
		plt.title("t = {}".format(t))
		plt.pause(0.01)