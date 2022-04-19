from cmath import cos
import math
import matplotlib.pyplot as plt

dt = 0.01
x=[]
y=[]
x.append(0)
y.append(0)
v0 = 30.0
theta = 45.0
g = 9.81

vx = v0*math.cos(math.pi*theta/180)
vy = []
vy.append(v0*math.sin(math.pi*theta/180))

for i in range(430):
    vy.append(vy[i] - g*dt)
    x.append(x[i] + vx*dt)
    y.append(y[i] + vy[i]*dt)

plt.plot(x,y)
plt.show()


