import numpy as np
import matplotlib.pyplot as plt
a=20
t = np.linspace(0, 2*np.pi, 1024)

y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
x = 16 * (np.sin(t)) ** 3
plt.figure(figsize=(4,4))
plt.plot(x,y,'k',color='r',linewidth='1',linestyle='-')
plt.show()
