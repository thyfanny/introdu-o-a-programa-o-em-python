x = int(input('Primeiro número: '))
y = int(input('Segundo número: '))

contador = 0
resultado = 0
while contador < y:
    resultado += x
    contador += 1
print(resultado)