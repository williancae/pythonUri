valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for nota in notas:
    quantidadeNotas = int(valor/nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidadeNotas,nota))
    valor -= quantidadeNotas * nota
print('MOEDAS:')
for moeda in moedas:
    quantidadeMoedas = int(round(valor, 2)/moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidadeMoedas, moeda))
    valor -= quantidadeMoedas * moeda