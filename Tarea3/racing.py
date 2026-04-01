from sys import stdin

class Arista:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __lt__(self, other):
        return self.peso > other.peso


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
    mst = []

    aristas.sort()

    for arista in aristas:
        u, v, peso = arista.u, arista.v, arista.peso

        if dsu.find(u) != dsu.find(v):
            mst.append(arista)
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
            circutio.append(Arista(u-1, v-1, peso))
            peso_total += peso

        peso_maximo = kruskal(nodos, circutio)


        print(peso_total - peso_maximo)

        casos -= 1

    nada = stdin.readline()

main()

