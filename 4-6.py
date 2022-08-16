distancia = float(input("Distância desejada(em km): "))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

print(f"O valor total a ser pago é R${'%.2f' % passagem}.")