from sys import stdin
from collections import deque

def construir_grafo(recetas):

    mapa_ids = {}
    siguiente_id = 0

    # Paso 1: asignar ID a cada plato
    for derived, base, _, cost, prestige in recetas:

        if base not in mapa_ids:
            mapa_ids[base] = siguiente_id
            siguiente_id += 1

        if derived not in mapa_ids:
            mapa_ids[derived] = siguiente_id
            siguiente_id += 1

    recetas_totales = siguiente_id

    # Paso 2: crear estructuras
    adj = [[] for _ in range(recetas_totales)]
    incidencias = [0] * recetas_totales

    # Paso 3: agregar aristas
    for derived, base, _, cost, prestige in recetas:

        u = mapa_ids[base]
        v = mapa_ids[derived]

        adj[u].append((v, cost, prestige))
        incidencias[v] += 1

    return adj, incidencias, mapa_ids


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

def dp(costos, prestigios, n, presupuesto):

    if n == len(costos):
        return 0
    elif costos[n] > presupuesto:
        return dp(costos, prestigios, n+1, presupuesto)
    else:
        return max(dp(costos, prestigios, n+1, presupuesto), costos[n] + dp(costos, prestigios, n+1, presupuesto - costos[n]))


def main():

    presupuesto = int(stdin.readline())


    while presupuesto:
        num_pizzas = int(stdin.readline())

        recetas = []

        for _ in range(num_pizzas):
            derived, base, ingredient, cost, prestige = stdin.readline().split()
            cost = int(cost)
            prestige = int(prestige)
            recetas.append((derived, base, ingredient, cost, prestige))

        adj, incidencias, id_map = construir_grafo(recetas)

        print(adj, incidencias, id_map)

        topo = topoSortKahn(adj, incidencias)
        print(topo)

        cost, prestige = calcular_costos_prestigios(adj, topo, incidencias)

        max = dp(cost, prestige, 0, presupuesto)
        print(max)

        presupuesto = int(stdin.readline())


main()