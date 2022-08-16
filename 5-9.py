x = int(input('Dividendo: '))
y = int(input('Divisor: '))

contador = 0
while x >= y:
    x -= y
    contador += 1

print(f"""O resultado da divisão é {contador}
Resto: {x}""")