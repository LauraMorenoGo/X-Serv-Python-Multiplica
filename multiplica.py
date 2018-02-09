#!/usr/bin/pithon3

print('Tabla de multiplicar')

for numero1 in range(1,11):
    print('La tabla de multiplicar del ', numero1)
    for numero2 in range(1,11):
        print(numero1, 'por', numero2, 'es ', numero1*numero2)
