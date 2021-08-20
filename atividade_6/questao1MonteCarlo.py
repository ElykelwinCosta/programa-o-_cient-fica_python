import numpy as np
import matplotlib.pyplot as plt


N = 100 #Largura do quadro
M = 100 #Altura do quadro

particulas = 1
particulasInfectadas = int(input("Qual a quantidade de partículas contaminadas iniciais? ")) #Partículas infectadas iniciais
passos = 1000

coordenadaXInfectada = np.random.randint(0, N, size = particulasInfectadas) 
coordenadaYInfectada = np.random.randint(0, N, size = particulasInfectadas)
coordenadaDasInfectadas = []  #Lista que recebe as coordenadas X,Y da/s partículas infectadas

for cordX, cordY in zip(coordenadaXInfectada, coordenadaYInfectada): #Varredura dos arrays com as coordenadas X, Y
  coordenadaDasInfectadas.append((cordX, cordY)) #Lançamento de uma tupla com X, Y na lista das coordenadas das partículas infectadas
  
x = np.zeros(particulas*passos) #Array com todas as coordenadas X ocupados por zeros
y = np.zeros(particulas*passos) #Array com todas as coordenadas Y ocupados por zeros

x.shape = (particulas, passos) #Quebra do array X com tamanho particulas por passos
y.shape = (particulas, passos) #Quebra do array Y com tamanho particulas por passos

moveX = np.random.randint(0, N, size = particulas * passos) #Atualização da lista de X ocupadas com zeros com os valores da coordenada
moveY = np.random.randint(0, N, size = particulas * passos) #Atualização da lista de Y ocupadas com zeros com os valores da coordenada

moveX.shape = (particulas, passos) #Quebra do array com os movimentos de X com tamanho particulas por passos
moveY.shape = (particulas, passos) #Quebra do array com os movimentos de Y com tamanho particulas por passos
axisLista = []  #Lista que recebe as coordenadas X,Y da/s partículas saudáveis

contaminadas = 0
for i in range (1, passos):  #A cada passo
  for p in range(0, particulas): #A cada partícula
    x[p, i] = (x[p, i-1] + (moveX[p, i]))%N #A coordenada x indíce [p,i] recebe o valor correspondente ao valor do moveX
    y[p, i] = (y[p, i-1] + (moveY[p, i]))%M #A coordenada y indíce [p,i] recebe o valor correspondente ao valor do moveY
    for k in coordenadaDasInfectadas:
      if((x[p, i], y[p, i]) == (k[0], k[1])):
        #comparador = ((x[p, i], y[p, i]) == (k[0], k[1]))
        contaminadas += 1

##    axisLista.append((x[p, i], y[p, i])) #Lança na lista axisLista uma tupla com as coordenadas x,y

##infectadas = (axisLista == coordenadaDasInfectadas)
##totalInfectadas = np.sum(infectadas)
##print(totalInfectadas)

##contaminadas = 0 #Contador de células contaminadas
##for axis in axisLista: #A cada coordenada na lista de coordenadas
##  for infAxis in coordenadaDasInfectadas: #A cada coordenada das partículas infectadas
##    if(axis == infAxis): #Se forém iguais
##      contaminadas += 1 #Aumenta em 1 o número de células contaminadas

probabilidade = contaminadas/passos
print("A probabilidade de contaminação em {} passos, num quadro de {} x {}:".format(passos, N, M))
print("Iniciando com {} particulas contaminadas é de: {:.2f}%".format(particulasInfectadas, probabilidade))
      
plt.title("Random Walk - {} passos, com {} células contaminadas inicialmente\n Total de contaminadas = {}".format(passos, particulasInfectadas, contaminadas))
plt.scatter(x, y, s=30, c="b", marker="P")
for coordenada in coordenadaDasInfectadas:
  plt.scatter(coordenada[0], coordenada[1], s=30, c="r", marker="o")
plt.legend(["Partículas não infectadas", "Partículas infectadas"])
plt.show()

