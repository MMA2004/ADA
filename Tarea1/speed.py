"""
Mateo Monroy Aristizabal
8987333
16/02/2026

Complejidad:

La función buscar_c implementa una bisección recursiva sobre un intervalo real.

En cada llamada recursiva:
- El intervalo de búsqueda se divide a la mitad.
- Se ejecuta la función calcular_error, que recorre todos los segmentos.

Si n es la cantidad de segmentos, entonces:

    calcular_error cuesta O(n)

La recurrencia de buscar_c es:

    T(m) = T(m/2) + O(n)

No se puede aplicar el Teorema maestro porque hay dos variables diferentes involucradas


"""

from sys import stdin



ERROR = 1e-9


def calcular_error(segmentos, c):
    total = 0
    for i in range(len(segmentos)):
        total += segmentos[i][0] / (segmentos[i][1] + c)
    return total




def buscar_c(l, r, segmentos, t):

    if r - l < ERROR:
        ans = l

    else:
        mid = (l + r) / 2

        if calcular_error(segmentos, mid) < t:
            ans = buscar_c(l, mid, segmentos, t)
        else:
            ans = buscar_c(mid, r, segmentos, t)

    return ans


def main():

    linea = stdin.readline()

    while linea:

        n, t = map(int, linea.split())

        segmentos = []
        for _ in range(n):
            d, s = map(int, stdin.readline().split())
            segmentos.append((d, s))

        min_s = min(s for _, s in segmentos)

        min_c = -min_s
        distancia_max = 0
        for d, _ in segmentos:
            distancia_max += d

        max_c = (distancia_max / t) - min_s


        c = buscar_c(min_c, max_c, segmentos, t)

        ans = round(c, 15)
        print(f"{ans:.9f}")

        linea = stdin.readline()


main()