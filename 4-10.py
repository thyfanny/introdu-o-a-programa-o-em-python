quantidade_consumida = float(input('Quantidade de energia consumida em kWh: '))
tipo = input('Tipo de instalação: ')   #R, I ou C

if tipo == 'R':
    if quantidade_consumida <= 500:
        preco = quantidade_consumida * 0.4
    else:
        preco = quantidade_consumida * 0.65
elif tipo == 'C':
    if quantidade_consumida <= 1000:
        preco = quantidade_consumida * 0.55
    else:
        preco = quantidade_consumida * 0.6
elif tipo == 'I':
    if quantidade_consumida <= 5000:
        preco = quantidade_consumida * 0.55
    else:
        preco = quantidade_consumida * 0.6

print(f'O total a ser pago é R${preco:.2f}.')