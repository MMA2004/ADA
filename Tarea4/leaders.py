"""
Mateo Monroy Aristizabal
8987333
02/05/2026
"""
from sys import stdin

def criterio(x):
    return (-len(x), x)

def check(sol, nuevo, prohibidos):
    ans = True
    for t in sol:
        if tuple(sorted((t, nuevo))) in prohibidos:
            ans = False
    return ans

def phi(inicio, sol, temas, prohibidos, s):
    global sols
    if len(sol) == s:
        sols.append(sol.copy())

    else:
        for i in range(inicio, len(temas)):
            if check(sol, temas[i], prohibidos):
                sol.append(temas[i])
                phi(i + 1, sol, temas, prohibidos, s)
                sol.pop()


def main():
    global sols
    casos = int(stdin.readline())

    for caso in range(casos):
        t, p, s = map(int, stdin.readline().split())

        temas = []
        for _ in range(t):
            temas.append(stdin.readline().strip().upper())

        prohibidos = set()
        for _ in range(p):
            a, b = stdin.readline().strip().upper().split()
            prohibidos.add(tuple(sorted((a, b))))

        temas.sort(key=criterio)

        sols = []
        phi(0, [], temas, prohibidos, s)


        print(f"Set {caso + 1}:")
        for grupo in sols:
            print(" ".join(grupo))
        print()


main()