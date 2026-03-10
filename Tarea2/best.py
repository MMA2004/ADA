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