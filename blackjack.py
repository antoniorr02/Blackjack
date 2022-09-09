import random
import os 

carta_valor = {'as':11, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5, 'seis':6, 'siete':7, 'ocho':8, 'nueve':9, 'diez':10, 'j':10, 'q':10, 'k':10}
cartas = list(carta_valor.keys())

cartas_jugador = []
cartas_cpu = []

cartas_jugador.append(cartas[random.randint(0,len(cartas)-1)])
total_puntos_jugador = carta_valor[cartas_jugador[0]]
print(f"Su primera carta es {cartas_jugador} con un valor de {total_puntos_jugador}")
confirmacion = input("¿Desea seguir cogiendo cartas? ")

while(confirmacion == 'si'):
    cartas_jugador.append(cartas[random.randint(0,len(cartas)-1)])

    if(cartas_jugador[len(cartas_jugador)-1] != 'as'):
        total_puntos_jugador += carta_valor[cartas_jugador[len(cartas_jugador)-1]]
    else:
        if(total_puntos_jugador + 11 < 21):
            total_puntos_jugador += 11
        else:
            total_puntos_jugador += 1

    print(f"Sus cartas son {cartas_jugador} con un valor de {total_puntos_jugador}")
    if(total_puntos_jugador >= 21):
        break
    confirmacion = input("¿Desea seguir cogiendo cartas? ")
    os.system('clear')

if (total_puntos_jugador > 21):
    print("Te has pasado de 21 puntos, pierdes")
    exit()
elif(total_puntos_jugador == 21):
    print("Blackjack!!! Has ganado.")
    exit()

cartas_cpu.append(cartas[random.randint(0,len(cartas)-1)])
total_puntos_cpu = carta_valor[cartas_cpu[0]]
while(total_puntos_cpu < 17):
    cartas_cpu.append(cartas[random.randint(0,len(cartas)-1)])
    
    if(cartas_cpu[len(cartas_cpu)-1] != 'as'):
        total_puntos_cpu += carta_valor[cartas_cpu[len(cartas_cpu)-1]]
    else:
        if(total_puntos_jugador + 11 < 21):
            total_puntos_cpu += 11
        else:
            total_puntos_cpu += 1

if (total_puntos_cpu > 21):
    print("Has ganado la cpu se ha pasado de 21 puntos")
    exit()

print(f"La suma de tus puntos es de {total_puntos_jugador}, con las cartas {cartas_jugador}")
print(f"La suma de tus puntos es de {total_puntos_cpu}, con las cartas {cartas_cpu}")

if (total_puntos_jugador > total_puntos_cpu):
    print("Enhorabuena, has ganado")
elif (total_puntos_jugador < total_puntos_cpu):
    print("La cpu gana")
else:
    print("Habéis empatado")