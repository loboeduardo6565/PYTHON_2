
#Lista y bucle for
repuestos = ["Amortiguadores","Alternadores","Muñones","Tripoides","Terminales"]

""" # Recorriendo la lista

for categoria in repuestos:
    print(f'Categorías Disponibles: {categoria}')

"""

""" # Ejecuta un for hasta coincidir con una condición.

for categoria in repuestos:
    print(f'Categorías Disponibles: {categoria}')
    if categoria == "Tripoides":
        break

"""


# Ejecuta un for hasta encontrar una excepción 

for categoria in repuestos:
    if categoria == "Tripoides":
        break
    print(f'Categorías Disponibles: {categoria}')

"""

numeros = 10
for numero in range(numeros):
    print(f"El número es: {numero}")
else:
    print("Final")

"""