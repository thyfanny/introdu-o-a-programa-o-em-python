x = int(input("Primeiro número: "))
y = int(input("Segundo número: "))
z = int(input("Terceiro número: "))

numeros = [x, y, z]
numeros.sort()
print(f'{numeros[0]} é o maior número e {numeros[2]} é o menor.')