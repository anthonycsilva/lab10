import random

def dado():
    lista_numeros = list()
    i = 0
    n = int(input('Quantos Numeros deseja?'))
    while i<n:
        numero = random.randint(1,6)
        lista_numeros.append(numero)
        i+= 1
    print(lista_numeros)
    return lista_numeros



def conta_faces(lista):
    resultado = list()
    for i in range(len(lista)):
        if lista[i-1] == lista[i] and lista[i] != lista[i+1]:
            resultado.append(lista[i])
    print(len(resultado))
    return resultado


conta_faces(dado())