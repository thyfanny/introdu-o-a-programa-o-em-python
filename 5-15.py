#programa para controlar uma pequena máquina registradora
#códigos do preços: 1 = 0.50 - 2 = 1 - 3 = 4 - 5 = 7 - 9 = 8
#exibe o total quando for digitado 0
#deve exibir uma mensaegm de erro 'Código inválido' caso seja qualquer outro número

total = 0

while True:
    codigo = int(input('Insira o código do produto: '))
    if codigo == 0 : break
    elif codigo == 1:
        total += 0.5
    elif codigo == 2:
        total += 1
    elif codigo == 3:
        total += 4
    elif codigo == 5:
        total += 7
    elif codigo == 9:
        total += 8
    else:
        print('Código inválido.')
        continue
    
print('Valor total a ser pago: ', total)