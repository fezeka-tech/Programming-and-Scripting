# This is a program that displays a plot of the functions f(x)=x, g(x)=x² , and h(x)=x^3 in the range [0,4] on one set of axes #

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0,4))

plt.plot(xpoints, colour= "orange")
plt.plot(xpoints, label= "xsquared", colour= "green")
plt.plot(xpoints, label= "xcubed", colour= "yellow")

plt.legend()

plt.show()







 
