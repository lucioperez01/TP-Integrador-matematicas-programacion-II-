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

def test():
    pass