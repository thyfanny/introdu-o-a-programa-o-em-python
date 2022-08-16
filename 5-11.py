#pergunta o depósito inicial e a taxa de juros de uma poupança
#exibe os valores mês a mês para os primeiros 24 meses

#formula
#montante = capital_aplicado * (1+taxa)**tempo_de_aplicação

deposito = float(input('Depósito inicial: '))
taxa = float(input('Taxa de juros: '))

tempo = 1

while tempo <= 24:
    montante = deposito * (1+(taxa/100))**tempo
    juros = montante - deposito
    print(f"Mês {tempo}:\nMontante: {round(montante, 2)}\nJuros: {round(juros, 2)}")
    tempo += 1

print(f"Montante final: {round(montante, 2)}")