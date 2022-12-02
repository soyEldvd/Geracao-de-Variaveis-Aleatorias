import matplotlib as plt
import math as math
import numpy as np
from time import time

#valores:
a = 65.238763884
c = 91209401
x = time()
m = 2**32
v1 = np.zeros(10000)
v2 = np.zeros(10000)

#gerando os pseudo-aleatorios
for i in range(10000):
    func = ((a * x + c) % m)
    x = func
    v1[i] = (func / (m -1))

#passando-os pela função exponencial 
for i in range(10000):
    v2[i] = (-1/3)* (math.log(1 - v1[i]))

#plotando o histograma
x = v2
plt.hist(x)
plt.show()

#plotando a cdf
count, binscount = np.histogram(x)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(binscount[1:], cdf)
plt.show()

#calculo da media
media = 0
for i in range (10000):
    media = media + v1[i]

media /= 10000

#calculo da variancia
var = 0
for i in range (10000):
    variancia = var + (v1[i] - media) ** 2

var /= 10000

#printando os valores
print(f"a media vale {media}\na variancia vale {var}")