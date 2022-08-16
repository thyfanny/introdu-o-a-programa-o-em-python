#calcula o tempo em segundos

print("Todos os números inseridos devem ser inteiros.")
dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

horas += dias*24
minutos += horas*60
segundos += minutos*60

print(f"O total em segundos é {segundos}")