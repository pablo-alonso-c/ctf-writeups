import random
import time

FLAG = "C3TF{############################}"

with open("./palabras.txt", "r", encoding="utf-8") as f:
    palabras = f.read().splitlines()

with open("./definiciones.txt", "r", encoding="utf-8") as f:
    definiciones = f.read().splitlines()

semilla = int(time.time())
random.seed(semilla)

print("Bienvenido al generador de palabras del día.\nGenerando palabras...")
time.sleep(3)

print("Las 3 palabras de hoy son: \n")

for i in range(3):
    indice = random.randint(0, len(palabras) - 1)

    palabra_del_dia = palabras[indice]
    definicion_del_dia = definiciones[indice]
    print(f"{palabra_del_dia}:\t{definicion_del_dia}")


print("\n¿Cuál será la palabra de mañana?")
respuesta = input("> ")

print("Viajando al futuro para validar la respuesta...")
time.sleep(2)

indice_siguiente = random.randint(0, len(palabras) - 1)
palabra_siguiente = palabras[indice_siguiente]

if respuesta == palabra_siguiente:
    print(f"¡Correcto! La flag es: {FLAG}")
    
    

else:
    print("Incorrecto. La palabra de mañana es: " + palabra_siguiente)
