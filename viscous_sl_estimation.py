import matplotlib
import matplotlib.pyplot as plt 
import math
import numpy as np
import time 
import os

from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

# Assumptions

u_freestream = 200    # in m/s
rho = 0.41   # in kg/m^3
l = 0.1   # in m
mu = 1.8e-5 # in kg/ms

y_plus = 5 # aus Schlichting 



# Calculations


def calc_wd(length, u_fr=u_freestream):
    Re = ( u_fr * rho * length ) / mu

    C_f = ( 2 * np.log10( Re ) - 0.65 )**-2.3    # Sking friction - Schlichting Assumption for Re < 10^9

    tau_w = ( C_f * rho * u_fr**2 ) / 2   # wall shear stress

    u_f = np.sqrt( tau_w / rho ) # friction velocity

    w_d = ( y_plus * mu ) / ( u_f * rho )

    return w_d


#2D - plotting

def plot2D(freestream):
    ts2d = time.time()
    x_array = np.arange(0.01, 3.5, 0.01)
    y_array = calc_wd(x_array,freestream)


    fig, ax = plt.subplots()
    ax.plot(x_array, y_array*1000000)

    ax.set(xlabel="length (m)", ylabel="wall distance (µm)", title="wall distance y for v = " + str(freestream) + " m/s")
    ax.grid()

    fig.savefig("plots/test_"+ str(ts2d) +".png")
    plt.show()
    print(x_array)
    print(y_array)


#3D - plotting

def plot3D():
    print("CP1")
    ts3d = time.time()
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    #Calc data
    X = np.arange(0.01, 3.5, 0.01)
    Y = np.arange(100,400,1)
    X,Y = np.meshgrid(X,Y)

    Z = calc_wd(X,Y)
    
    print("CP2")
    #plot the surface

    surf = ax.plot_surface(X,Y,Z*1000000,  cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set(xlabel = "length (m)", ylabel = "freestream velocity (m/s)", zlabel = "wall distance (µm)")

    print("CP3")

    #Colorbar which maps values to color
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()



# MAIN 

print("Wall distance is: " + str(calc_wd(0.1)))

plot3D()

#plot2D(200)

#plot2D(300)

