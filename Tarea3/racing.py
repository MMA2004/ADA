"""
Mateo Monroy Aristizabal
8987333
04/04/2026

"""

from sys import stdin
from heapq import heappush, heappop

INF = float('inf')

def prim(s, n, adj):
    d = [-INF] * n
    p = [-1] * n
    visitado = [False] * n

    total = 0
    d[s] = 0

    cola = []
    heappush(cola, (0, s))

    while cola:
        peso, u = heappop(cola)
        peso = -peso

        if not visitado[u]:

            visitado[u] = True

            if peso == d[u]:
                total += peso

                for pesoAux, v in adj[u]:
                    if not visitado[v] and pesoAux > d[v]:
                        p[v] = u
                        d[v] = pesoAux
                        heappush(cola, (-d[v], v))

    return total


def main():
    casos = int(stdin.readline())

    while casos:

        nodos, aristas = map(int, stdin.readline().split())

        circutio = [[] for _ in range(nodos)]
        peso_total = 0

        for _ in range(aristas):
            u, v, peso = map(int, stdin.readline().split())

            circutio[u-1].append((peso, v-1))
            circutio[v-1].append((peso, u-1))
            peso_total += peso

        peso_maximo = prim(0, nodos, circutio)

        print(peso_total - peso_maximo)

        casos -= 1

    stdin.readline()


main()