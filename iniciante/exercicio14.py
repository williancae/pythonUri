a = int(input())
h = a // 3600  #  dividimos o valor com // para pegarmos o valor inteiro da divisão
resto = a % 3600 # pegamos o resto das horas Obs: o resto de Horas e minutos e segundos
m = resto // 60 # pegamos o minuto com divisão inteira
s = resto % 60 # o que resta de horas e minutos é segundo
print('{}:{}:{}'.format(h,m,s))

