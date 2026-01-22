import matplotlib.pyplot as plt
import numpy as np
phi=np.linspace(0, 2*np.pi, 100)
#1
def func(x):
    return np.sqrt(np.abs(x)**3)

x = np.linspace(-8, 8, 100)
y = func(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x)")
plt.grid()
plt.show()
#3
r= func(phi)

plt.figure()
ax = plt.subplot(111,projection='polar')
ax.plot(phi,r)
ax.set_title("Polar graph of task 3")
plt.show()

#4

cos_val=np.cos(2*phi)

r=np.sqrt(9*cos_val)
r[cos_val<=0]=0

plt.figure()
ax=plt.subplot(111, projection='polar')
ax.plot(phi, r)
ax.set_title("Polar Plot of r = sqrt(9 * cos(2φ))")
plt.show()

