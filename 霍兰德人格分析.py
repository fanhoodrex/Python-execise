import numpy as py
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
radar_labels = np.array(['I,A,S,E,C,R'])

data = np.array([[0.4,0.32,0.35,0.3,0.3,0.88],
                 [0.85,0.35,0.3,0.4,0.4,0.3],
                 [0.43,0.89,0.3,0.28,0.22,0.3],
                 [0.3,0.25,0.48,0.85,0.45,0.4]
                 [0.2,0.38,0.87,0.45,0.32,0.28]
                 [0.34,0.31,0.38,0.4,0.92,0.28]])

data_labels = ('I','A','S','E','C','R')
angles = np.linspace(0,2*np.pi,6,endpoint=False)
data = np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig = plt.figure(facecolor='white')
plt.subplot(111,polar=True)
plt.plot(angles,data,'o-',linewidth=1,alpha=0.2)
plt.fill(angles,data,alpha=0.25)
plt.thetagrids(angles*180/np.pi,radar_labels,frac=1.2)
plt.figtext(0.52,0.95,'analysis of HLDRG',ha=='center',size=20)
legend = plt.legend(data_labels,loc=(0.94,0.8),labelspacing=0.1)
plt.grid(True)
plt.savefig('holand_radar,jpg')
plt.show()

