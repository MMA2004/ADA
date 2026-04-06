"""
Mateo Monroy Aristizabal
8987333
02/04/2026

Complejidad:

Primero se ordena la lista de trabajos según su fecha límite (deadline).
Este ordenamiento tiene un costo de O(n log n), donde n es la cantidad de trabajos.

Luego se ejecuta la función max_tareas, que recorre todos los trabajos una sola vez.
En cada iteración se realizan operaciones sobre una cola de prioridad (heap),
como inserciones (heappush) y posibles eliminaciones (heappop), cada una con
costo O(log n).

Dado que se realizan a lo sumo n inserciones y n eliminaciones en el heap,
el costo total de esta fase es O(n log n).

Por lo tanto, la complejidad total del algoritmo es:

O(n log n)

"""

from sys import stdin
from heapq import heappush,heappop


def max_tareas(trabajos):

    suma_total = 0
    heap = []
    for d, q in trabajos:
        suma_total += q
        heappush(heap, -q)
        if suma_total > d:
            q = heappop(heap)
            suma_total += q

    return len(heap)


def main():

    casos = int(stdin.readline())

    while casos:
        nada = stdin.readline()

        N = int(stdin.readline())
        trabajos = []
        for _ in range(N):
            q, d = map(int, stdin.readline().split())
            trabajos.append((d, q))

        trabajos.sort()

        ans = max_tareas(trabajos)

        print(ans)


        casos -= 1


main()