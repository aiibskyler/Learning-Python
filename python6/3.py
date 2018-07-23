#乒乓选手雷达图
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
labels=np.array(['速度','力量','天赋','成绩'])
nAttr=4
data=np.array([7,5,6,9])
angles=np.linspace(0,2*np.pi,nAttr,endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure(facecolor="white")
plt.subplot(111,polar=True)
plt.plot(angles,data,'bo-',color='g',linewidth=2)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.25,0.95,'乒乓球能力分析雷达图',ha='center')
plt.grid(True)
plt.show()
