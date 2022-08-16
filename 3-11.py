#calcula o desconto

preco = float(input('Preço da mercadoria: '))
porcentagem = float(input('Percentual de desconto: '))/100

print(f"O desconto é de {'%.2f' %(preco*porcentagem)}")
print(f"O preço com o desconto fica {'%.2f' %(preco - (preco*porcentagem))}")