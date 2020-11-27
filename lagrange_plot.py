import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

x = np.array([-1, 2, -2])
y = np.array([0, 5, -3])
poly = lagrange(x, y)
print(poly)
poly.coef

x_plot = np.linspace(-20,20,1000)
y_plot = []
for i in x_plot:  
  sum = 0
  for pos,val in enumerate(poly.coef[::-1]):
    sum += val*i**(pos)
  y_plot.append(sum)


ig,ax = plt.subplots(figsize=(12,8))

xmin, xmax, ymin, ymax =-5,5,-5,5

ticks_frequency = 1

ax.scatter(x,y, c="r",label="Pontos")
ax.plot(x_plot,y_plot,label="Função encontrada",c='k')

ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('x', size=14, labelpad=15)
ax.set_ylabel('y', size=14, labelpad=15, rotation=0)
ax.xaxis.set_label_coords(1.03, 0.512)
ax.yaxis.set_label_coords(0.5, 1.02)

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
x_ticks_major = x_ticks[x_ticks != 0]
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
y_ticks_major = y_ticks[y_ticks != 0]
ax.set_xticks(x_ticks_major)
ax.set_yticks(y_ticks_major)
ax.set_xticks(np.arange(xmin,xmax+1), minor=True)
ax.set_yticks(np.arange(ymin,ymax+1), minor=True)

ax.grid(which='major', color='grey', linewidth=1, linestyle='-', alpha=0.2)
ax.grid(which='minor', color='grey', linewidth=1, linestyle='-', alpha=0.2)

ax.plot((1), (0), linestyle="", marker=">", markersize=4, color="k",
        transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot((0), (1), linestyle="", marker="^", markersize=4, color="k",
        transform=ax.get_xaxis_transform(), clip_on=False)

ax.legend()
