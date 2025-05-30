def dni_a_set(dni):
    dni=str(dni)
    conjunto = []
    for i in range(len(dni)):
        numero_actual = int(dni[i])
        if numero_actual not in conjunto:
            conjunto.append(numero_actual)
            j = len(conjunto) - 1
            #ordenamiento tipo insersion
            while j > 0 and conjunto[j] < conjunto[j - 1]:
                conjunto[j], conjunto[j - 1] = conjunto[j - 1], conjunto[j]
                j -= 1
    return set(conjunto)

L = dni_a_set(43029505)
V = dni_a_set(33224659)
D = dni_a_set(43230009)
M1 = dni_a_set(36869470)
M2 = dni_a_set(32237875)

print(f"L = {L}\nV = {V}\nD = {D}\nM1 = {M1}\nM2 = {M2}")

def expresiones():
    
    print("Iniciales disponibles: L, V, D, M1, M2")

    persona1 = input("Elegi a la primer persona (L, V, D, M1, M2): ")
    persona2 = input("Elegi a la segunda persona (L, V, D, M1, M2): ")

    # Creo un diccionario para los conjutnos
    conjuntos = {   
        "L": L,
        "V": V,
        "D": D,
        "M1": M1,
        "M2": M2
    }

    if persona1 in conjuntos and persona2 in conjuntos:  # valido inputs
        c1 = conjuntos[persona1]
        c2 = conjuntos[persona2]

        print(f"\nConjunto de {persona1}: {c1}")
        print(f"Conjunto de {persona2}: {c2}")

        #Interseccion
        interseccion = c1 & c2  # realizo la operacion
        print(f"\n1) que digitos tienen {persona1} y {persona2} en comun?") # imprimo la pregunta
        print(f"→ {interseccion if interseccion else 'no tienen digitos e comun'}") # imprimo la respuesta

    else:
        print("Error: Iniciales invalidas - Las opciones son L, V, D, M1 o M2.")

# Llamo a la funcion
expresiones()