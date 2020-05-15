"""
Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
"""

a = float(input())
b = float(input())
c = float(input())
media = (a * 2 + b * 3 + c * 5) / 10
print("MEDIA = %0.1f"%media)