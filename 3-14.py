km_percorridos = float(input('Km percorridos: '))
dias = int(input('Quantidade de dias pelos quais o carro foi alugado: '))

print(f"O valor total a ser pago é {'%.2f' % ((km_percorridos * 0.15)+(dias * 60))}")