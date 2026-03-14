"""
Mateo Monroy Aristizabal
10/03/2026

Complejidad:

La memorizacion usa como clave la pareja (i,k) que representa el stackholder i y cuanto porcenatje acumulado me falta

Puede haber i * k estados diferentes:

i puede tomar 0 <= i <= n siendo n la cantidad de stakeholders

y k puede tomar K valores que es la capacidad que queda para llegar al 50%

Por lo que la cantidad de estados que se guardan en la memoria es O(n * k)

Cada estado hace trabajo O(1):

ya que solo se hacen sumas, comparaciones y asignaciones.

Por ende la complejidad temporal es:

O(n * K)

"""

from sys import stdin


def dp(i, k, x, A, memo):

    if (i, k) in memo:
        ans = memo[(i, k)]

    else:
        if k <= 0:
            ans = 0
            memo[(i, k)] = ans

        elif i == len(A):
            ans = float("inf")
            memo[(i, k)] = ans

        elif i == x:
            ans = dp(i+1, k, x, A, memo)
            memo[(i, k)] = ans

        else:
            ans = min(dp(i + 1, k, x, A, memo), dp(i + 1, k - A[i], x, A, memo) + A[i])
            memo[(i, k)] = ans

    return ans


def main():
    n, x = map(int, stdin.readline().split())

    while n != 0 and x != 0:


        porcentajes = []
        for _ in range(n):
            porcentajes.append(float(stdin.readline()) * 100)

        memo = {}

        ans = dp(0, 5000.1 - porcentajes[x-1], x-1, porcentajes, memo)

        res = (porcentajes[x-1] / (porcentajes[x-1] + ans)) * 100

        print(f"{res:.2f}")

        n, x = map(int, stdin.readline().split())


main()