import numpy as np
import matplotlib.pyplot as plt
# A função plot foi baseada no seguinte repositorio: https://stackoverflow.com/questions/13430231/how-i-can-get-cartesian-coordinate-system-in-matplotlib

class NewtonPoli():
  def __init__(self,pontos):
    self.pontos = np.array(pontos,float)
    self.coeff = self.coefi()
    self.grau = len(self.coeff) - 1
  
  @property
  def x(self):
    return self.pontos[:,0]
  @property
  def y(self):
    return self.pontos[:,1]

  def coefi(self):
    a = self.y.copy()
    m =  len(a)
    for k in range(1,m):
      a[k:m] = (a[k:m] -a[k-1])/(self.x[k:m]-self.x[k-1])
    return a
  
  def _prod(self,v):
    prod = 1 
    for i in v:
      prod *= i
    return prod
  
  def f(self,x0):
    p = 0
    for pos in range(len(self.coeff)):
      if pos == 0: 
        p += self.coeff[0]
      else: 
        p += self.coeff[pos]*self._prod(-self.x[0:pos]+x0)
    return p 

  def __repr__(self):
    return f"Polinômio de {self.grau}º grau \nCom os coeficientes: {self.coeff}"
  
  def plot(self,comeco=0,final=0):
    
    fig,ax = plt.subplots(figsize=(12,8))

    xmin, xmax, ymin, ymax = -self.x[-1]+1,self.x[-1]+1,-self.x[-1]+1,self.x[-1]+1
    x_plot = np.linspace(xmin,xmax,100)
    y_plot = np.array([self.f(i) for i in x_plot])
    ticks_frequency = 1

    ax.scatter(self.x, self.y, c="r",label="Pontos")
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

if __name__ == "__main__":
  P = NewtonPoli(list(zip([1,4,6],[0,5,-3])))
  print(P)
  P.plot()
