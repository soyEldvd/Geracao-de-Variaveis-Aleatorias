import matplotlib.pyplot as plt
import numpy as np
from time import time
#entrando com os valores
a = 1029
c = 3333
x = time()
m = 2**64
v1 = np.zeros(10000)#definindo um vetor de tamanho

for i in range(10000):
    func = ((a * x + c) % m)
    x = func
    v1[i] = (4 + (func / (m -1)) * 8) #dessa forma, faço com que os valores que estavam de 0 a 1 fiquem entre o intervalo de k1 a k2

#plotando o histograma da distribuição:
x = v1
plt.hist(x)
plt.show()

#plotando a cdf
count, binscount = np.histogram(x)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(binscount[1:], cdf)
plt.show()

#calculando a media
media = 0
for i in range (10000):
    media = media + v1[i]

media /= 10000

#calculando a variancia 
variancia = 0
for i in range(10000):
    variancia = variancia + (v1[i] - media) ** 2

variancia /= 10000

print(f"media {media} \n variancia {variancia}")