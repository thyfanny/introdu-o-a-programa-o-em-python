n = int(input('Tabuada de: '))
inicio = int(input('Início: '))
fim = int(input('Fim: '))

contador = inicio

while contador <= fim:
    print(f'{n}x{contador} = {n*contador}')
    contador += 1