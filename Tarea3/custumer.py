from sys import stdin
from heapq import heappush,heappop

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

        suma_total = 0
        heap = []
        for d, q in trabajos:
            suma_total += q
            heappush(heap, -q)
            if suma_total > d:
                q = heappop(heap)
                suma_total += q

        print(len(heap))


        casos -= 1


main()