salario = float(input("Salário atual: "))

if salario > 1250:
    aumento = '%.2f' % (salario + (salario * 0.1))
if salario <= 1250:
    aumento = '%.2f' % (salario + (salario * 0.15))
print(f'O novo salário é R${aumento}.')