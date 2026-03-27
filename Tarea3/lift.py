from sys import stdin
from heapq import heappush,heappop

INF = float('inf')


def dijkstra(n, T, pisos, pisos_dict, pos, peores_tiempos):

    dist = {}
    pqueue = []

    # Inicialización desde piso 0
    for ascensor in range(n):
        if 0 in pisos[ascensor]:
            dist[(0, ascensor)] = peores_tiempos[ascensor][0]
            heappush(pqueue, (dist[(0, ascensor)], (0, ascensor)))

    # Dijkstra
    while len(pqueue) != 0:
        du, (piso, ascensor) = heappop(pqueue)

        if (piso, ascensor) in dist or dist[(piso, ascensor)] == du:

            # 1. moverse dentro del ascensor
            idx = pos[(piso, ascensor)]

            # anterior
            if idx > 0:
                nuevo_piso = pisos[ascensor][idx - 1]
                v = (nuevo_piso, ascensor)
                duv = abs(piso - nuevo_piso) * T[ascensor]

                if v not in dist or du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))

            # siguiente
            if idx < len(pisos[ascensor]) - 1:
                nuevo_piso = pisos[ascensor][idx + 1]
                v = (nuevo_piso, ascensor)
                duv = abs(piso - nuevo_piso) * T[ascensor]

                if v not in dist or du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))

            # 2. cambiar de ascensor
            for ascensor_nuevo in pisos_dict[piso]:
                if ascensor_nuevo != ascensor:

                    v = (piso, ascensor_nuevo)
                    duv = 5 + peores_tiempos[ascensor_nuevo][piso]

                    if v not in dist or du + duv < dist[v]:
                        dist[v] = du + duv
                        heappush(pqueue, (dist[v], v))

    return dist



# Implementación algoritmo de Dijkstra para la versión uno a uno
def dijkstra1(G, s, t):
    dist = [INF for _ in range(len(G))]
    dist[s] = 0
    pqueue, found = list(), False
    # for u in range(len(G)): heappush(pqueue, (dist[u], u))
    heappush(pqueue, (dist[s], s))

    while len(pqueue) != 0 and not found:
        du, u = heappop(pqueue)
        if u == t:
            found = True
        else:
            if dist[u] == du:
                for v, duv in G[u]:
                    if du + duv < dist[v]:
                        dist[v] = du + duv
                        heappush(pqueue, (dist[v], v))
    return dist[t]



def main():
    linea = stdin.readline()

    while linea:
        n, k = map(int, linea.split())

        T = list(map(int, stdin.readline().split()))

        pisos = []
        for _ in range(n):
            pisos.append(list(map(int, stdin.readline().split())))

        pisos_ascensores = {}

        for ascensor in range(n):
            for piso in pisos[ascensor]:
                if piso not in pisos_ascensores:
                    pisos_ascensores[piso] = []
                pisos_ascensores[piso].append(ascensor)

        peores_tiempos = [{} for _ in range(n)]

        for ascensor in range(n):
            for piso in pisos[ascensor]:
                max_distancia = max(abs(piso - otro_piso) for otro_piso in pisos[ascensor])
                peores_tiempos[ascensor][piso] = max_distancia * T[ascensor]

        pos_idx = {}
        for ascensor in range(n):
            idx = 0
            for piso in pisos[ascensor]:
                pos_idx[(piso, ascensor)] = idx
                idx += 1

        dist = dijkstra(n, T, pisos, pisos_ascensores, pos_idx, peores_tiempos)

        ans = INF
        for ascensor in range(n):
            if (k, ascensor) in dist:
                if dist[(k, ascensor)] < ans:
                    ans = dist[(k, ascensor)]

        if ans == INF:
            print("IMPOSSIBLE")
        else:
            print(ans)

        linea = stdin.readline()

main()