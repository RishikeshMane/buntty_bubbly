import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4])
y=np.array([2,5,1,6])

plt.subplot(1,2,1)
plt.plot(x,y,)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('this is plot 1')

a=np.array([1,2,1,1.5])
b=np.array([4,1,1,3])

plt.subplot(1,2,2)
plt.plot(a,b,)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('this is plot 2')

plt.show()