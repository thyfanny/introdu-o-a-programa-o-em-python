#imprime os números da entrada, e depois faz a soma e média aritimetica deles

lista = []

while True:
    entrada = int(input('Insira um número: '))
    if entrada == 0 : break
    lista.append(entrada)
    print(entrada)

soma = sum(lista)
media = soma//len(lista)

print('Soma: ', soma)
print('Média aritmetica: ', media)