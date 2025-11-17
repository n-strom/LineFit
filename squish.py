import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("MCSV.csv", delimiter=",", dtype=str)

#print(data[0])

x = data[1:, 0].astype (np.float32)
y = data[1:, 2].astype (np.float32)

#print("y =", y)
#print("x =", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

#EXCERCISE 1

print(print_equation(slope, intercept, data[0,2], data[0,0]))
#The equation of the line is: y =  -0.005218172899576858 height (mm)/mass (g) x +  6.073048655438714 mass (g)
#None

#EXCERCISE 2

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("Mass (g)")
plt.ylabel("Height (cm)")
plt.show()
