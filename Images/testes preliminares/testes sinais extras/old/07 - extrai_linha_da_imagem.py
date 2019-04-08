# Cria vetor com amostras de uma linha de uma imagem

from string import split
from pylab import *
import numpy
import matplotlib.pyplot as plt
import Image
from sys import exit as fim

# ----------- Le imagem
I = Image.open('.\senoXY-0-10T45.png')
width , height = I.size
print "largura = ", width , "pixels"
print "altura = ", height , "pixels"
W = width
H = height

# ------------- Seleciona linha l
j = int(H/2)

# ------------- Cria vetor V com pontos da imagem
V = []
for m in range (W):
    V.append(0)
for i in range(W) :
    V[i] = I.getpixel((i,j))    


# saida grafica
plt.plot(V)
plt.show()

fim()
