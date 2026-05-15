"""
Mateo Monroy Aristizabal
8987333
03/05/2026
"""
from sys import stdin

class DSU:
    def __init__(self, n):
        self.padre = list(range(n + 1))
        self.rango = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.procesado = [False] * (n + 1)

    def find(self, v):
        if v == self.padre[v]:
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
            self.size[u] += self.size[v]

            if self.rango[u] == self.rango[v]:
                self.rango[u] += 1


def validez(padre, peso_minimo, aristas, dsu, n):
    ans = True
    u = 1
    while u <= n and ans:
        if dsu.find(u) == padre:
            t = len(aristas[u])
            i = 0
            while i < t and ans:
                v, w = aristas[u][i]
                if dsu.find(v) == padre and w < peso_minimo:
                    ans = False
                i += 1
        u += 1
    return ans

def phi(n, pesos, aristas):
    dsu = DSU(n)
    ans = 0

    pesos_ordenados = sorted(pesos.keys(), reverse=True)

    for peso_actual in pesos_ordenados:
        padres = set()


        for u, v in pesos[peso_actual]:

            padres.add(dsu.find(u))
            padres.add(dsu.find(v))
            dsu.union(u, v)


        for candidato in padres:
            padre = dsu.find(candidato)
            if not dsu.procesado[padre]:
                if validez(padre, peso_actual, aristas, dsu, n):
                    ans += dsu.size[padre]
                dsu.procesado[padre] = True


        for candidato in padres:
            dsu.procesado[dsu.find(candidato)] = False

    return ans

def main():
    t = int(stdin.readline())

    for _ in range(t):
        n, m = map(int, stdin.readline().split())

        pesos = {}
        aristas = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, stdin.readline().split())
            aristas[u].append((v, w))
            aristas[v].append((u, w))
            if w not in pesos:
                pesos[w] = []
            pesos[w].append((u, v))

        resultado = phi(n, pesos, aristas)
        print(resultado)


main()