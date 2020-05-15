"""
Também não consegui entender está lógica, porém fiz da seguinte maneira e deu certo:

Se a distância recebida é a diferença entre os dois carros, então quer dizer que consigo a mesma distância multiplicando o tempo pela diferença das duas velocidades, portanto:

Distância = Tempo(Y - X)

Isola-se o Tempo e tem-se a formula abaixo:

Tempo = Distância / (Y - X)

Porém queremos o tempo em minutos; para isso é só convertermos as velocidades (km/h para km/m). Portanto precisamos levar em conta que 1h equivale 60 minutos (km/h -> km/60m), então:

Tempo = Distância / ((Y / 60.0) - (X / 60.0))
"""

distancia = int(input())
x = 60
y = 90
tempo = distancia/((y/60) - (x/60))
print("%d minutos"%tempo)