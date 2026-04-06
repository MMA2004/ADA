"""
Mateo Monroy Aristizabal
8987333
02/04/2026

Complejidad:

Primero se ejecuta el algoritmo de Kruskal, el cual realiza un ordenamiento de las aristas según su peso.
Este paso tiene un costo de O(m log m), donde m es la cantidad de aristas. Luego recorre todas las aristas
una sola vez. Para cada arista se realizan operaciones find y union sobre
la estructura DSU.

En consecuencia, la complejidad total del algoritmo es:

O(m log m)

"""

from sys import stdin


class DSU:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0]*n

    def find(self, v):
        if self.padre[v] == v:
            ans = v
        else:
            self.padre[v] = self.find(self.padre[v])
            ans = self.padre[v]
        return ans

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            if self.rango[u] < self.rango[v]:
                u, v = v, u

            self.padre[v] = u
            if self.rango[u] == self.rango[v]:
                self.rango[u] += 1


def kruskal(nodos, aristas):
    dsu = DSU(nodos)
    total = 0

    aristas.sort(reverse=True)

    for peso, u, v in aristas:

        if dsu.find(u) != dsu.find(v):
            total += peso
            dsu.union(u, v)

    return total

def main():

    casos = int(stdin.readline())

    while casos:

        nodos, aristas = map(int, stdin.readline().split())

        circutio = []
        peso_total = 0

        for _ in range(aristas):
            u, v, peso = map(int, stdin.readline().split())
            circutio.append((peso, u-1, v-1))
            peso_total += peso

        peso_maximo = kruskal(nodos, circutio)

        print(peso_total - peso_maximo)

        casos -= 1

    nada = stdin.readline()

main()

