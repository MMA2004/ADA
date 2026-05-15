"""
Mateo Monroy Aristizabal
8987333
02/05/2026
"""
from sys import stdin

def check_limites_visitado(r, c, m, n, visited):
    return 0 <= r < m and 0 <= c < n and not visited[r][c]


def check_checkpoint(r, c, pasos, checkpoints):
    ans = True
    encontrado = False
    i = 0
    n = len(checkpoints)

    while i < n and not encontrado and ans:
        s, ri, ci = checkpoints[i]

        if pasos == s:
            if (r, c) != (ri, ci):
                ans = False
            encontrado = True

        elif (r, c) == (ri, ci):
            ans = False

        i += 1

    return ans


def check_distancia(r, c, pasos, checkpoints):
    posible = True
    encontrado = False
    i = 0
    n = len(checkpoints)

    while i < n and not encontrado:
        s, ri, ci = checkpoints[i]

        if pasos < s:
            encontrado = True
            dist = abs(r - ri) + abs(c - ci)
            pasos_restantes = s - pasos
            if dist > pasos_restantes:
                posible = False

        i += 1

    return posible

def check_bloqueo(r, c, m, n, visited):

    horizontal = (check_limites_visitado(r, c - 1, m, n, visited) and
                  check_limites_visitado(r, c + 1, m, n, visited) and
                  not check_limites_visitado(r - 1, c, m, n, visited) and
                  not check_limites_visitado(r + 1, c, m, n, visited))

    vertical = (check_limites_visitado(r - 1, c, m, n, visited) and
                check_limites_visitado(r + 1, c, m, n, visited) and
                not check_limites_visitado(r, c - 1, m, n, visited) and
                not check_limites_visitado(r, c + 1, m, n, visited))

    return horizontal or vertical


def phi(r, c, pasos, visited, checkpoints, m, n, total):
    ans = 0

    if pasos == total:
        if (r, c) == (0, 1):
            ans = 1


    elif (r, c) == (0, 1) and pasos < total:
        ans =  0

    else:
        visited[r][c] = True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            n_pasos = pasos + 1

            if check_limites_visitado(nr, nc, m, n, visited):
                if check_checkpoint(nr, nc, n_pasos, checkpoints):
                    if check_distancia(nr, nc, n_pasos, checkpoints):
                        if not check_bloqueo(nr, nc, m, n, visited):
                            ans += phi(nr, nc, n_pasos, visited, checkpoints, m, n, total)

        visited[r][c] = False
    return ans



def main():
    m, n = map(int, stdin.readline().split())
    caso = 1
    while m != 0 and n != 0:

        r1, c1, r2, c2, r3, c3 = map(int, stdin.readline().split())

        total = m * n

        # tiempos de checkpoints
        t1 = total // 4
        t2 = (total * 2) // 4
        t3 = (total * 3) // 4

        checkpoints = [
            (t1, r1, c1),
            (t2, r2, c2),
            (t3, r3, c3)
        ]

        visited = [[False] * n for _ in range(m)]

        ans = phi(0, 0, 1, visited, checkpoints, m, n, total)

        print(f"Case {caso}: {ans}")
        caso += 1

        m, n = map(int, stdin.readline().split())



main()

