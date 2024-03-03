import numpy as np
import matplotlib.pyplot as plt

def expplot_v1(x):
    return np.exp(-x)

def expplot_v2(x):
    return 1/np.exp(-x)

def expplot_v3(x):
    return 1/(1+np.exp(-x))


X = np.arange(-5.0, 5.0, 0.1)
Y1 = expplot_v1(X)
Y2 = expplot_v2(X)
Y3 = expplot_v3(X)
plt.subplot(121)
plt.plot(X, Y1, linestyle =':', label='exp(-x)')
plt.plot(X, Y2, linestyle ="--", label='1/exp(-x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('exp(-x) & 1/exp(-x)')
plt.legend()

plt.subplot(122)
plt.plot(X, Y3, linestyle ="-.", label='1/1+exp(-x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('1/(1+exp(-x))')
plt.legend()

plt.show()