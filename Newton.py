from math import *
import numpy as np
import matplotlib.pyplot as plt

"""
A função dada pelo úsuario deve possuir a mesma sintaxe padrão do pyhton 
Ex: x^2 deve ser escrito como x**2 

"""

def deriv(f,x,h=1e-10):
  """ Solução aproximada de uma derivada
  Parametros: 
  f : string 
    Função a qual iremos achar a derivada (Essa deve ser um string)
  x: número 
    Ponto que queromos a devidada
  h: número
    tolerncia 
  """
  f_deriv = f.replace("x","(x+h)")
  return (eval(f_deriv)-eval(f))/h
   
def newton_(f,x,tol=1e-6,max_inte=10e6):
  """ Solução aproximada para f(x) = 0
  Parametros: 
    f : string 
      Função a qual iremos achar a raiz (Essa deve ser um string) 
    x : número
      Valor da suposição inicial 
    tol: número 
      Critério de parada, f(x) < tol
    max_inte: número 
      Número máximo de interações
  """
  x_plot = np.arange(-x,x)
  try: 
    while abs(eval(f)) >= tol and max_inte != 0 : 
      x = x - eval(f)/deriv(f,x)
      result = x
      max_inte -= 1
  except NameError: 
    print(f"{f} Não é um função valida")
  print(f"\n x = {x} \t f(x) = {eval(f)}")

  if max_inte == 0: 
    print("Número máximo de interações excedido, nem uma solução foi encotrada")
    return False 
  return x

def plot_newton(funcao,x0):

  x = newton_(funcao,x0)
  if x:
    #Criar alguns pontos proximos ao número suposto
    x_ = np.arange(-2*x0,2*x0,1e-1) 
    y_ = [eval(funcao) for x in x_] 
    
    # Criar a figura
    fig = plt.figure(figsize = (12, 8)) 
    ax = fig.add_subplot()

    #Algunas configurações para mudar o padrão da função plot
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['bottom'].set_color('black')
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    ax.spines['left'].set_color('black')

    #Plotar o grafico da função e a raiz encontrada 
    ax.plot(x_,y_)
    ax.plot(x,eval(funcao),'or')
    plt.title(f"Newton-Raphson gráfico para função {funcao}")
    plt.show()

def main():
  funcao = input("Digite uma função f(x):  ")
  x0 = float(eval(input("Digite o ponto inicial: ")))
  
  #Checar se a função não é uma constante 
  try: 
    int(funcao)
  except ValueError: 
    plot_newton(funcao,x0)
  else: print("Função não é valida")

if __name__ == "__main__":
  main()
