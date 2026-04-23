"""
Mateo Monroy Aristizabal
8987333
22/04/2026
"""

from sys import stdin

def phi(sol, n, m, i, check):
    if len(sol) == m:
        ans = list(sol)
    else:
        k, ans = 0, []
        while k < 10 and len(ans) == 0:
            if i != 1 or k != 0:
                sol.append(k)
                newCheck = check * 10 + k
                if i < n or newCheck % i == 0:
                    ans = phi(sol, n, m, i + 1, newCheck)
                sol.pop()
            k += 1
    return ans

def phi2(sol, n, m, i, acumulador):
    if acumulador == m:
        ans = sol
    else:
        k, ans = 0, 0
        while k < 10 and ans == 0:
            if i != 1 or k != 0:
                sol = sol * 10 + k
                if i < n or sol % i == 0:
                    ans = phi(sol, n, m, i + 1, acumulador + 1)
                sol = sol // 10
            k += 1
    return ans

def main():
    casos = int(stdin.readline())
    for i in range(casos):
        n, m = map(int, stdin.readline().split())

        ans = phi([], n, m, 1, 0)
        res = 0

        if len(ans) == 0:
            res = -1
        else:
            for j in ans:
                res = res * 10 + j

        print(f"Case {i + 1}: {res}")

main()