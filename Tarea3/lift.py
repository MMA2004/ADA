"""
Mateo Monroy Aristizabal
8987333
02/04/2026

Complejidad:

Sea n el número de ascensores y m el número de pisos por ascensor.

Primero se construyen las estructuras pisos_conectores, peores_tiempos y pos_idx,
recorriendo los pisos de cada ascensor. Esto tiene un costo de O(n·m).

Luego se ejecuta el algoritmo de Dijkstra sobre un grafo donde cada nodo
representa un par (piso, ascensor), por lo que el número de nodos es O(n·m).

Desde cada nodo se puede mover a dos pisos dentro del mismo ascensor,
y además cambiar de ascensor en el mismo piso, lo cual en el peor caso implica
hasta n conexiones. Por lo tanto, el número de aristas es O(n²·m).

Utilizando una cola de prioridad, Dijkstra tiene un costo de
O((V + E) log V), lo que en este caso corresponde a:

O(n^2·m log(n·m))

Por lo tanto, la complejidad total del algoritmo es:

O(n^2·m log(n·m))

"""

from sys import stdin
from heapq import heappush,heappop

INF = float('inf')


def dijkstra(n, T, pisos, pisos_conectores, pos, peores_tiempos):

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

        if dist[(piso, ascensor)] == du:

            # 1. moverse dentro del ascensor
            idx = pos[(piso, ascensor)]

            # piso de abajo
            if idx > 0:
                nuevo_piso = pisos[ascensor][idx - 1]
                v = (nuevo_piso, ascensor)
                duv = abs(piso - nuevo_piso) * T[ascensor]

                if v not in dist or du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))

            # piso de arriba
            if idx < len(pisos[ascensor]) - 1:
                nuevo_piso = pisos[ascensor][idx + 1]
                v = (nuevo_piso, ascensor)
                duv = abs(piso - nuevo_piso) * T[ascensor]

                if v not in dist or du + duv < dist[v]:
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))

            # 2. cambiar de ascensor
            for ascensor_nuevo in pisos_conectores[piso]:
                if ascensor_nuevo != ascensor:

                    v = (piso, ascensor_nuevo)
                    duv = 5 + peores_tiempos[ascensor_nuevo][piso]

                    if v not in dist or du + duv < dist[v]:
                        dist[v] = du + duv
                        heappush(pqueue, (dist[v], v))

    return dist


def main():
    linea = stdin.readline()

    while linea:
        n, k = map(int, linea.split())

        T = list(map(int, stdin.readline().split()))

        pisos = []
        for _ in range(n):
            pisos.append(list(map(int, stdin.readline().split())))

        if k == 0:
            ans = 0
        else:
            pisos_conectores = {}

            for ascensor in range(n):
                for piso in pisos[ascensor]:
                    if piso not in pisos_conectores:
                        pisos_conectores[piso] = []
                    pisos_conectores[piso].append(ascensor)

            peores_tiempos = [{} for _ in range(n)]

            for ascensor in range(n):
                piso_inicial = pisos[ascensor][0]
                piso_final = pisos[ascensor][-1]
                for piso in pisos[ascensor]:
                    max_distancia = max(piso - piso_inicial, piso_final - piso)
                    peores_tiempos[ascensor][piso] = max_distancia * T[ascensor]

            pos_idx = {}
            for ascensor in range(n):
                idx = 0
                for piso in pisos[ascensor]:
                    pos_idx[(piso, ascensor)] = idx
                    idx += 1

            dist = dijkstra(n, T, pisos, pisos_conectores, pos_idx, peores_tiempos)

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