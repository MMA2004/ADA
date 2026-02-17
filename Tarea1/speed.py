"""
Mateo Monroy Aristizabal
8987333
16/02/2026
"""

from sys import stdin



ERROR = 1e-9


def calcular_error(segmentos, c):
    total = 0
    for i in range(len(segmentos)):
        total += segmentos[i][0] / (segmentos[i][1] + c)
    return total




def solve(l, r, segmentos, t):

    if r - l < ERROR:
        ans = l

    else:
        mid = (l + r) / 2

        if calcular_error(segmentos, mid) < t:
            ans = solve(l, mid, segmentos, t)
        else:
            ans = solve(mid, r, segmentos, t)

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


        c = solve(min_c, max_c, segmentos, t)

        ans = round(c, 15)
        print(f"{ans:.9f}")

        linea = stdin.readline()


main()