#Paquetes Basicos------------------------------
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

#Para el manejo de algebra lineal---------------
from numpy.linalg import *
from scipy.linalg import expm,inv

#Para los plots 3D -----------------------------
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N=1000
#-------------- punto 2-----------------

x=uniform(0,9,N)
ruido=uniform(-2,2,N)#+np.sin(x1)
y=x+ruido*np.exp(-0.1*(x-5)**2)
z=x+y+uniform(-3,3,N)*np.exp(0.05*(-(x-np.mean(x))**2-(y-np.mean(y))**2))

#--------------Punto 3-------------------

restaz=(z-np.mean(z))/np.sqrt(np.var(z))
restay=(y-np.mean(y))/np.sqrt(np.var(y))
restax=(x-np.mean(x))/np.sqrt(np.var(x))

#-------------Punto 4--------------------
mat=([restaz,restay,restax])
MatCov=np.cov(mat)
print MatCov

#-------------Punto 5--------------------
eigenvalues, eigenvectors= np.linalg.eig(MatCov)
print eigenvalues, eigenvectors

#-------------Punto 5--------------------

