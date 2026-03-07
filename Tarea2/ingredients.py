"""
Mateo Monroy Aristizabal
05/03/2026

Complejidad:
Se usa el algoritmo de Kahn para obtener el orden topologico:
V son los nodos (sabores de las pizzas)
E son las aristas (son lo que cambia al pasar de una receta a otra)
O(V + E)

Luego se usa la funcion calcular_costos_prestigios
O(V + E)

Luego se usa la funcion dp:
Los estados que se guardan en la memoria son:
(n, presupuesto)

donde:

n puede tomar V valores
presupuesto puede tomar B valores

O(V * B)

Cada estado hace trabajo O(1).

Complejidad final:
O(V * B)

V es el numero de pizzas diferentes
B es el presupuesto maximo.
"""


from sys import stdin
from collections import deque

def topoSortKahn(G, incidencias):
    queue = deque()
    topo = []

    # Copiamos indegree porque lo vamos a modificar
    inc = incidencias[:]

    # Inicializar cola con raíces
    for u in range(len(G)):
        if inc[u] == 0:
            queue.append(u)

    while queue:
        u = queue.popleft()
        topo.append(u)

        for (v, c, p) in G[u]:
            inc[v] -= 1
            if inc[v] == 0:
                queue.append(v)

    if len(topo) == len(G):
        ans = topo
    else:
        ans = []
    return ans

def calcular_costos_prestigios(G, topo, incidencias):
    INF = float("inf")

    costos = [INF] * len(G)
    prestigios = [0] * len(G)

    # Inicializar solo raíces reales
    for u in range(len(G)):
        if incidencias[u] == 0:
            costos[u] = 0
            prestigios[u] = 0

    # Relajación en orden topológico
    for u in topo:
        for (v, c, p) in G[u]:
            newCost = costos[u] + c
            newPrestige = prestigios[u] + p

            if newCost < costos[v]:
                costos[v] = newCost
                prestigios[v] = newPrestige
            elif newCost == costos[v] and newPrestige > prestigios[v]:
                prestigios[v] = newPrestige

    return costos, prestigios

def dp(costos, prestigios, n, presupuesto, memo):
    if (n, presupuesto) in memo:
        ans = memo[(n, presupuesto)]
    else:
        if n == len(costos):
            ans = (0, 0)
        elif costos[n] > presupuesto:
            ans = dp(costos, prestigios, n+1, presupuesto, memo)
        else:
            # opción 1: no tomar plato
            p1, c1 = dp(costos, prestigios, n + 1, presupuesto, memo)

            # opción 2: tomar plato
            p2, c2 = dp(costos, prestigios, n + 1, presupuesto - costos[n], memo)
            p2 += prestigios[n]
            c2 += costos[n]

            # comparar
            if p2 > p1:
                ans = (p2, c2)
            elif p2 < p1:
                ans = (p1, c1)
            else:
                ans = (p2, min(c1, c2))

    memo[(n, presupuesto)] = ans

    return ans


def main():

    presupuesto = stdin.readline()


    while presupuesto:
        presupuesto = int(presupuesto)
        num_pizzas = int(stdin.readline())

        mapa_ids = {}
        siguiente_id = 0

        adj = []
        incidencias = []

        for _ in range(num_pizzas):
            derived, base, ingredient, cost, prestige = stdin.readline().split()
            cost = int(cost)
            prestige = int(prestige)

            # crear nodo base si no existe
            if base not in mapa_ids:
                mapa_ids[base] = siguiente_id
                siguiente_id += 1
                adj.append([])
                incidencias.append(0)

            # crear nodo derived si no existe
            if derived not in mapa_ids:
                mapa_ids[derived] = siguiente_id
                siguiente_id += 1
                adj.append([])
                incidencias.append(0)

            u = mapa_ids[base]
            v = mapa_ids[derived]

            # agregar arista
            adj[u].append((v, cost, prestige))

            # actualizar grado de entrada
            incidencias[v] += 1

        topo = topoSortKahn(adj, incidencias)

        cost, prestige = calcular_costos_prestigios(adj, topo, incidencias)
        memo = {}
        max, min = dp(cost, prestige, 0, presupuesto, memo)
        print(max)
        print(min)

        presupuesto = stdin.readline()


main()