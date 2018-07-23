#绘制正弦波
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5)
y=np.sin(x)
plt.figure(figsize=(8,4))
plt.plot(x,y,'k',color='r',linewidth='1',linestyle='-')
plt.show()
