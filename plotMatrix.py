import numpy as np
import matplotlib.pyplot as plt


X1, X2 = np.meshgrid(np.linspace(-3.0, 3.0, 30), np.linspace(-3.0, 3.0, 30))
A = [[0, 0], [0, 0]]
dX1 = A[0][0] * X1 + A[0][1] * X2
dX2 = A[1][0] * X1 + A[1][1] * X2

plt.xlabel("x_1")
plt.ylabel("x_2")

plt.axis('square')
plt.axis([-3, 3, -3, 3])

plt.streamplot(X1, X2, dX1, dX2, color='b', linewidth=0.5, density=2)
plt.savefig('fig1.png')
plt.show()

