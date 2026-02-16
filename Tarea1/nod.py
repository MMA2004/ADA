"""
Mateo Monroy Aristizabal
8987333
14/02/2026

Complejidad:

La funcion generar_nod y generar_secuencia se ejecutan una sola vez y estas dependen de LIMIT que es 1.000.000.

Temporal:
generar_nod es O(LIMIT log(LIMIT))


Espacial:
generar_nod es O(LIMIT)


La funcion buscar_index es una busqueda binaria recursiva:

T(n) = T(n/2)

Lo que segun el teroema maestro da:

a = 1
b = 2
k = 0

por lo que b^k = a

lo que nos da una complejidad de O(log n)

"""

from sys import stdin

LIMIT = 1000000

def generar_nod():
    nod = [0] * (LIMIT + 1)

    for i in range(1, LIMIT + 1):
        for j in range(i, LIMIT + 1, i):
            nod[j] += 1

    return nod


def generar_secuencia(nod):
    secuencia = []
    i = 1
    while i <= LIMIT:
        secuencia.append(i)
        i += nod[i]
    return secuencia


def buscar_index(l, r, v, A):
    if r - l == 1:
        # Caso base: comparamos el único elemento del rango
        if A[l] < v:
            ans = l + 1
        else:
            ans = l

    else:
        mid = (l + r) // 2


        if v < A[mid]:
            ans = buscar_index(l, mid, v, A)
        else:

            ans = buscar_index(mid, r, v, A)

    return ans

def main():
    casos = stdin.readline()

    nod = generar_nod()

    secuencia = generar_secuencia(nod)


    for i in range(int(casos)):
        inicio, final = stdin.readline().split()

        index1 = buscar_index(0, len(secuencia), int(inicio), secuencia)
        index2 = buscar_index(0, len(secuencia), int(final) + 1, secuencia)

        print(f"Case {i + 1}: {index2 - index1}")


main()