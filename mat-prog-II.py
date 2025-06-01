#recibe un dni, ordena y elimina repetidos. Retorna un set con el conjunto ↓
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

def suma_digitos_dni(dni):
    dni = str(dni)
    acumulador = 0
    for i in range(0, len(dni)):
        numero_actual = int(dni[i])
        acumulador += numero_actual 
    return acumulador

def frecuencia_digitos_dni(dni):
    dni = str(dni)
    frecuencia = {}
    for i in dni:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1
    return frecuencia


print("• Ingreso de DNIs de los integrantes: ")
lucio_dni = 43029505
valentin_dni = 33224659
danilo_dni = 43230009
matias_dni = 36869470
marcos_dni = 32237875

print(f"DNI de Lucio = {lucio_dni}\nDNI de valentin = {valentin_dni}\nDNI de Danilo = {danilo_dni}\nDNI de Matias = {matias_dni}\nDNI de Marcos = {marcos_dni}")
print(f"\n• Suma de los digitos de cada DNI: \nDNI de Lucio : {suma_digitos_dni(lucio_dni)}\nDNI de Valentin: {suma_digitos_dni(valentin_dni)}\nDNI de Danilo: {suma_digitos_dni(danilo_dni)}")
print(f"DNI de Matías: {suma_digitos_dni(matias_dni)}\nDNI de Marcos: {suma_digitos_dni(marcos_dni)}")

print(f"\n• Conteo de frecuencia de digitos de cada DNI: \nDNI de Lucio : {frecuencia_digitos_dni(lucio_dni)}\nDNI de Valentin: {frecuencia_digitos_dni(valentin_dni)}\nDNI de Danilo: {frecuencia_digitos_dni(danilo_dni)}")
print(f"DNI de Matías: {frecuencia_digitos_dni(matias_dni)}\nDNI de Marcos: {frecuencia_digitos_dni(marcos_dni)}")



#conversion a conjuntos con la funcion "dni_a_set" ↓
print("\n• Conjuntos en base a los DNI:")
L = dni_a_set(lucio_dni)
V = dni_a_set(valentin_dni)
D = dni_a_set(danilo_dni)
M1 = dni_a_set(matias_dni)
M2 = dni_a_set(marcos_dni)

print(f"L = {L}\nV = {V}\nD = {D}\nM1 = {M1}\nM2 = {M2}\nM1 = Matias y M2 = Marcos")

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
print("\n• Operaciones con los conjuntos formados a partir de los DNI ingresados: ")
expresiones()


