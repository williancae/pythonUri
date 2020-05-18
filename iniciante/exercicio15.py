a = int(input())
ano = a // 365
resto = a % 365
mes = resto // 30
dias = resto%30
print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano,mes,dias))
