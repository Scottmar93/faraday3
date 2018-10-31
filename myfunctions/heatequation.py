import numpy as np
import matplotlib.pyplot as plt


def heat1D_solver(dx, dt, length, t, T0, BC, alpha):

    time = np.arange(t[0], t[-1] + dt, dt)
    x = np.arange(0, length + dx, dx)

    T = np.ones([np.size(time), np.size(x)])*T0
    T[:, 0] = BC[0]
    T[:, -1] = BC[1]

    for i in range(0, np.size(time)-1):
        T[i+1, 1:-1] = (alpha*dt/dx**2)*(T[i, 2:] + T[i, 0:-2]) + (1 - 2*alpha*dt/dx**2)*T[i, 1:-1]

        # plot current time every 60 seconds
        if time[i+1] % 60 == 0:
            plt.clf()
            plt.plot(x, T[i+1, :])
            plt.ylim([10, np.max(BC)*1.1])
            plt.title('Time = {} seconds'.format(time[i+1]))
            plt.xlabel('x')
            plt.ylabel('T')
            plt.pause(0.005)

    return x, t, T


# Parameters and step sizes
dx = 0.01
dt = 1
length = 0.5
t = [0, 3600]
T0 = 10
BC = [50, 50]
alpha = 1.172*10**(-5)


# solve
x, t, temperature = heat1D_solver(dx, dt, length, t, T0, BC, alpha)

# plot final time
plt.plot(x, temperature[-1,:])
plt.show()



