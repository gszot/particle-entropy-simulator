import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return x+y


def plot3d():
#do wykr 3d
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [11,20,3,32,5,15,7,16,18,20]
    X, Y = np.meshgrid(x, y)
    print(type(X))
    Z = f(X, Y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_title('surface')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


def plot2d(x, y):
    fig = plt.figure()
    ax1 = plt.subplot(1, 1, 1)
    ax1.plot(x, y)
    ax1.set(title='entropy')
    ax1.grid()
    plt.show()
