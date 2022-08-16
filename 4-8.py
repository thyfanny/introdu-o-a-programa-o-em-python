x = float(input('Primeiro número: '))
y = float(input('Segundo número: '))
operacao = input('Tipo de operação (+, -, * ou /): ')

if operacao == '+':
    print(f'O resultado da soma é {x+y}.')
elif operacao == '-':
    print(f'O resultado da subtração é {x-y}.')
elif operacao == '*':
    print(f'O resultado da multiplicação é {x*y}.')
elif operacao == '/':
    print(f'O resultado da divisão é {x/y}.')