from datetime import date
from itertools import product

#Año bisiesto
def bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or  (anio % 400 == 0)

#Entrada de los años de nacimiento
L = 2000
V = 1990
D = 2001
M1 = 1992
M2 = 1986

anios = {1986, 1990, 1992, 2000, 2001}

print("• Ingreso de años de nacimiento de los integrantes: ")
print(f"\nAño de nacimiento de Lucio = {L}")
print(f"Año de nacimiento de Valentín = {V}")
print(f"Año de nacimiento de Danilo = {D}")
print(f"Año de nacimiento de Matías = {M1}")
print(f"Año de nacimiento de Marcos = {M2}")

def main():
    #Cuenta de pares e impares
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\n• ¿Cuántos integrantes nacieron en años pares e impares?")
    print(f"\nCantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")

    #Cálculo de generaciones
    print(f"\n• ¿A qué generación pertenecen los integrantes?")
    if all(anio >= 2000 for anio in anios):
        print(f"\nGrupo Z")
    else:
        print(f"\nHay distintas generaciones en este grupo")

    #Chequeo de año bisiesto
    print(f"\n• ¿Algún integrante nació en año bisiesto?")
    if any(bisiesto(anio) for anio in anios):
        print(f"\nTenemos un año especial -> {anio}")
    else:
        print(f"\nNo tenemos años especiales")

    #Calculo de edades
    anioActual = date.today().year
    edades = {anioActual - anio for anio in anios}

    #Producto cartesiano
    productoCartesiano = list(product(anios, edades))

    print("\n• Producto cartesiano (año, edad):")
    print(f"\n{set(productoCartesiano)}")

main()