import horas

horario = int(input("Digite as horas que deseje que sejam convertidas para minutos e segundos.\n"))

minutos, segundos = horas.calcular_horas(horario)

print(f"Este horário convertido fica assim:\nMinutos: {minutos} | Segundos: {segundos}")
