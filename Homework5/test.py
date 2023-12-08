import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,100,0.1)
y=np.sin(x)
Z=np.cos(x)
plt.plot(x,y)
plt.plot(x,Z)
plt.xlabel('x')
plt.grid(True)
plt.legend(['sin(x)','cos(x)'])
plt.show()