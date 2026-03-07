"""
Mateo Monroy Aristizabal
05/03/2026

El estado está definido por el par: (l,r)

donde: 0 <= l <= r <= n

Esto representa todos los subintervalos de un arreglo.

Por lo tanto:
Numero de estados = O(n²)

Dentro del estado (l, r) se ejecuta:
for i in range(l, r + 1):
El tamaño del intervalo es: r - l + 1
En el peor caso puede ser n.

Por cada i solo se hacen:

operaciones O(1)

dos llamadas recursivas

Entonces el costo por estado es:

O(r - l + 1) <= O(n)

Complejidad total:
Estados posibles O(n²)
Costo por estado: O(n)
Entonces: O(n³)


Espacio
El memo guarda todos los intervalos: O(n²)
"""

from sys import stdin

def giant(l, r, k, memo):

    if memo[l][r] != -1:
        ans = memo[l][r]
    else:
        if l >= r:
            ans = 0
        else:
            length = r - l + 1
            best = float("inf")

            for i in range(l, r + 1):

                cost = length * (k + i) + giant(l, i - 1, k, memo) + giant(i + 1, r, k, memo)

                if cost < best:
                    best = cost

            ans = best

        memo[l][r] = ans

    return ans


def main():

    casos = int(stdin.readline())

    for c in range(casos):

        n, k = map(int, stdin.readline().split())

        memo = [[-1]*(n+2) for _ in range(n+2)]

        m = giant(1, n, k, memo)

        print(f"Case {c+1}: {m}")


main()