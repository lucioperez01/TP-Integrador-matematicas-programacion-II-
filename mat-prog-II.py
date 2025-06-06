#recibe un dni, ordena y elimina repetidos. Retorna un set con el conjunto ↓
def dni_a_set(dni):
    dni = str(dni)
    conjunto = []
    for i in range(len(dni)):
        numero_actual = int(dni[i])
        if numero_actual not in conjunto:
            conjunto.append(numero_actual)
            j = len(conjunto) - 1
            while j > 0 and conjunto[j] < conjunto[j - 1]:
                conjunto[j], conjunto[j - 1] = conjunto[j - 1], conjunto[j]
                j -= 1
    return set(conjunto)

def suma_digitos_dni(dni):
    return sum(int(d) for d in str(dni))

def frecuencia_digitos_dni(dni):
    dni = str(dni)
    frecuencia = {}
    for i in dni:
        frecuencia[i] = frecuencia.get(i, 0) + 1
    return frecuencia

# Carga de DNIs
lucio_dni = 43029505
valentin_dni = 33224659
danilo_dni = 43230009
matias_dni = 36869470
marcos_dni = 32237875

print("• Ingreso de DNIs de los integrantes: ")
print(f"DNI de Lucio = {lucio_dni}")
print(f"DNI de Valentin = {valentin_dni}")
print(f"DNI de Danilo = {danilo_dni}")
print(f"DNI de Matías = {matias_dni}")
print(f"DNI de Marcos = {marcos_dni}")

# Suma
print(f"\n• Suma de los dígitos:")
print(f"Lucio: {suma_digitos_dni(lucio_dni)}")
print(f"Valentin: {suma_digitos_dni(valentin_dni)}")
print(f"Danilo: {suma_digitos_dni(danilo_dni)}")
print(f"Matías: {suma_digitos_dni(matias_dni)}")
print(f"Marcos: {suma_digitos_dni(marcos_dni)}")

# Frecuencia
print(f"\n• Frecuencia de dígitos:")
print(f"Lucio: {frecuencia_digitos_dni(lucio_dni)}")
print(f"Valentin: {frecuencia_digitos_dni(valentin_dni)}")
print(f"Danilo: {frecuencia_digitos_dni(danilo_dni)}")
print(f"Matías: {frecuencia_digitos_dni(matias_dni)}")
print(f"Marcos: {frecuencia_digitos_dni(marcos_dni)}")

# Conjuntos
L = dni_a_set(lucio_dni)
V = dni_a_set(valentin_dni)
D = dni_a_set(danilo_dni)
M1 = dni_a_set(matias_dni)
M2 = dni_a_set(marcos_dni)

print(f"\n• Conjuntos:")
print(f"L = {L}")
print(f"V = {V}")
print(f"D = {D}")
print(f"M1 = {M1}")
print(f"M2 = {M2}\n(M1 = Matías, M2 = Marcos)")

# Diccionario global de conjuntos
conjuntos = {
    "L": L,
    "V": V,
    "D": D,
    "M1": M1,
    "M2": M2
}

# Función de operaciones
def expresiones():
    print("\n• Operaciones con los conjuntos:")
    print("Iniciales disponibles: L, V, D, M1, M2")

    persona1 = input("Elegí la primera persona: ").upper()
    persona2 = input("Elegí la segunda persona: ").upper()

    if persona1 in conjuntos and persona2 in conjuntos:
        c1 = conjuntos[persona1]
        c2 = conjuntos[persona2]

        print(f"\nConjunto de {persona1}: {c1}")
        print(f"Conjunto de {persona2}: {c2}")

        #Unión
        union = c1 | c2
        print(f"\n1) ¿Cuál es la unión entre los conjuntos de {persona1} y {persona2}?")
        print(f"→ {union if union else 'Los conjuntos son idénticos.'}")
        
        # Intersección
        interseccion = c1 & c2
        print(f"\n1) ¿Qué dígitos tienen {persona1} y {persona2} en común?")
        print(f"→ {interseccion if interseccion else 'No tienen dígitos en común'}")

        # Diferencia simétrica
        simetrica = c1 ^ c2
        print(f"\n👉 ¿Qué dígitos aparecen en uno u otro, pero no en ambos?")
        print(f"{simetrica if simetrica else 'Los dos conjuntos son idénticos.'}")

        # Diferencia
        diferencia1 = c1 - c2
        diferencia2 = c2 - c1
        print(f"\n👉 ¿Qué dígitos tiene {persona1} y no {persona2}?")
        print(f"{diferencia1 if diferencia1 else 'Ninguno'}")
        print(f"\n👉 ¿Qué dígitos tiene {persona2} y no {persona1}?")
        print(f"{diferencia2 if diferencia2 else 'Ninguno'}")
    else:
        print("Error: Iniciales inválidas. Usá L, V, D, M1 o M2.")

# Llamada
expresiones()


