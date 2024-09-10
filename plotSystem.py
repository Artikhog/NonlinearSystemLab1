import numpy as np
import matplotlib.pyplot as plt

lim = 3

X1, X2 = np.meshgrid(np.linspace(-lim, lim, 30), np.linspace(-lim, lim, 30))
# dX1 = (X1-X2)*(1-X1**2-X2**2)
# dX2 = (X1+X2)*(1-X1**2-X2**2)
dX1 = -X1**3+X2**3
dX2 = X2**3 * X1 - X2**3

plt.axis('square')
plt.axis([-lim, lim, -lim, lim])
# circle1 = plt.Circle((0, 0), 1, color='b', fill=False)
# plt.gca().add_patch(circle1)

plt.streamplot(X1, X2, dX1, dX2, color='r', linewidth=0.5, density=1.5)
plt.savefig('fig_system.png')
plt.show()
