velocidade = float(input("Velocidade em km/h: "))

if velocidade > 80:
    multa = '%.2f' % ((velocidade - 80) * 5)
    print(f'Multado em R${multa}.')