#!/usr/bin/env python3
import random, time

VISTAS = ["templar", "impulsora", "picacaballos"]   # las 3 palabras mostradas

palabras = open("palabras.txt", encoding="utf-8").read().splitlines()
N = len(palabras)

ahora = int(time.time())
for s in range(ahora + 2, ahora - 600, -1):          # ventana hacia atras
    random.seed(s)
    if [palabras[random.randint(0, N-1)] for _ in range(3)] == VISTAS:
        print("Respuesta:", palabras[random.randint(0, N-1)])   # la 4a palabra
        break
else:
    print("No encontrada. Revisa palabras.txt o amplia la ventana.")
