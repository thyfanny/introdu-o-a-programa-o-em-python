valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Quantidade de anos a pagar: '))
meses = anos * 12
prestacao_mensal = valor_casa/meses
limite = salario * 0.3

if prestacao_mensal > limite:
    print('O empréstimo não poderá ser realizado pois a prestação mensal ultrapassa 30% do salário do usuário.')
else:
    print(f"A prestação mensal ficou no valor de R${prestacao_mensal:.2f} durante {anos} anos.")