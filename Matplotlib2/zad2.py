import numpy as np
import matplotlib.pyplot as plt

np.random.seed(194526)


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 12

for c, m, zlow, zhigh in [('c', '3', -20, -50), ('m', 'H', -15, -25), ('orange', '^', -23, -14),
                          ('b', "p", 0, -17), ('y', 'o', -12, 2)]:
    xs = randrange(n,5, 10)
    ys = randrange(n,0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, color=c, marker=m)

ax.set_xlabel('oś X')
ax.set_ylabel('oś Y')
ax.set_zlabel('oś Z')
plt.show()