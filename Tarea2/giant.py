from sys import stdin


def giant(l, r, k, memo):

    if (l, r) in memo:
        ans = memo[(l, r)]
    else:
        if l >= r:
            ans = 0
        else:
            min_actual = float("inf")
            for i in range(l, r + 1):

                candidato = (r - l + 1) * (k + i) + giant(l, i - 1, k, memo) + giant(i + 1, r, k, memo)

                min_actual = min(min_actual, candidato)
            memo[(l, r)] = min_actual
            ans = min_actual

    return ans

def main():

    casos = int(stdin.readline())

    for c in range(casos):

        n, k = map(int, stdin.readline().split())

        memo = {}

        m = giant(1, n, k, memo)

        print(f"Case {c+1}: {m}")


main()