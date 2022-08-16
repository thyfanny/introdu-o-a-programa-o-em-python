cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Há quantos anos é fumante? '))
tempo_minutos = cigarros_por_dia*anos*3650
dias = (tempo_minutos/60)//24
print(f'Você perdeu {int(dias)} dias de vida por causa do cigarro.')