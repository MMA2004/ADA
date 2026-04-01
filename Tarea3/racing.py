from sys import stdin

class Arista:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __lt__(self, other):
        return self.peso > other.peso



def kruskal(nodos, aristas):
    idArbol = [0 for _ in range(nodos)]
    mst = []
    total = 0

    for i in range(nodos):
        idArbol[i] = i

    aristas.sort()

    for arista in aristas:
        u, v, peso = arista.u, arista.v, arista.peso
        if idArbol[u] != idArbol[v]:
            mst.append(arista)
            total += peso
            p1 = idArbol[u]
            p2 = idArbol[v]
            for i in range(nodos):
                if idArbol[i] == p1:
                    idArbol[i] = p2


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

