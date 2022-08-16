#calcula o aumento do salário

salario = float(input("Valor do salário: "))
porcentagem = (float(input("Porcentagem de aumento: ")))/100

print(f'O valor do aumento foi de {salario*porcentagem}')
print(f'Então, o novo salário é {salario+(salario*porcentagem)}')