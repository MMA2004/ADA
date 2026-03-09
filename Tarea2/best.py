from sys import stdin


def dp(i, k, x, A):

    if k <= 0:
        return 0

    elif i == len(A):
        return float("inf")

    elif i == x:
        return dp(i+1, k, x, A)

    else:

        return min(dp(i + 1, k, x, A), dp(i + 1, k - A[i], x, A) + A[i])


def main():
    n, x = map(int, stdin.readline().split())

    while n != 0 and x != 0:


        porcentajes = []
        for _ in range(n):
            porcentajes.append(float(stdin.readline()) * 100)


        ans = dp(0, 5000.1 - porcentajes[x-1], x-1, porcentajes)

        res = (porcentajes[x-1] / (porcentajes[x-1] + ans)) * 100

        print(f"{res:.2f}")

        n, x = map(int, stdin.readline().split())


main()