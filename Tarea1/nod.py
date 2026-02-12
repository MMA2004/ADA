from sys import stdin

LIMIT = 1000000

def generar_tabla():
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

        # Si el valor buscado es menor o igual a la mitad,
        # se busca en la parte H ** (1 / mid_k) - W ** (1 / mid_k)izquierda (incluyendo la mitad)
        if v < A[mid]:
            ans = buscar_index(l, mid, v, A)
        else:
            # Si es mayor, se busca en la derecha
            ans = buscar_index(mid, r, v, A)

    return ans

def main():
    casos = stdin.readline()

    nod = generar_tabla()

    secuencia = generar_secuencia(nod)


    for i in range(int(casos)):
        inicio, final = stdin.readline().split()

        index1 = buscar_index(0, len(secuencia), int(inicio), secuencia)
        index2 = buscar_index(0, len(secuencia), int(final) + 1 , secuencia)

        print(f"Case {i + 1}: {index2 - index1}")


main()