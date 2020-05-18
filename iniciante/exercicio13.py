valor = int(input())
print(valor)
notas = [100,50,20,10,5,2,1]

for nota in notas:
    quantidadeNotas = int(valor/nota)
    print("{} nota(s) de R$ {},00".format(quantidadeNotas,nota))
    valor -= quantidadeNotas * nota
"""dinheiro = int(input())
# dinheiro = 20 #Valor inicial
a = dinheiro/100 #20/100 = 0.20  [0] mostra na tela
b = a%100 #20%100 = 0.20 [20]
c = b/50 #20/50 = 0.40 [0] mosrtra  na tela
d = c%50 #20%50 = 0.40 [40]
e = d/20 #20/20 = 1 [1] mostra na tela
f = e%20 #20%20 = 0 [0]
g = f/10 #0
h = g%10 #0
i = h/5 #0
j = i%5 #0
k = j/2 #0
l = k%2 #0
print("Dinheiro = %d"%dinheiro)
print("Nota de 100: %d\n"%a,
      "Nota de 50: %d\n"%c,
      "Nota de 20: %d\n"%e,
      "Nota de 10: %d\n"%g,
      "Nota de 5:  %d\n"%i,
      "Nota de 2:  %d\n"%k,
      "Nota de 1:  %d"%l)
"""