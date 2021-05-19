import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=plt.figaspect(0.5))
c1 = fig.add_subplot(2, 3, 1, projection='3d')
c2 = fig.add_subplot(2, 3, 2, projection='3d')
c3 = fig.add_subplot(2, 3, 3, projection='3d')
c4 = fig.add_subplot(2, 3, 4, projection='3d')
c5 = fig.add_subplot(2, 3, 5, projection='3d')
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
c1.bar3d(x, y, bottom, width, depth, top, color='pink', shade=True)
c2.bar3d(x, y, bottom, width, depth, top, color='orange', shade=False)
c3.bar3d(x, y, bottom, width, depth, top, color='g', shade=True)
c4.bar3d(x, y, bottom, width, depth, top, color='y', shade=False)
c5.bar3d(x, y, bottom, width, depth, top, color='darkblue', shade=True)
plt.show()