from sys import stdin


def phi(i, j, memo, T, R):
    if i < 0 or j < 0:
        return 0
    if (i,j) in memo:
        return memo[(i, j)]
    if T[i] == R[j]:
        memo[(i, j)] = 1 +  phi(i-1, j - 1, memo, T, R)
    else:
        memo[(i,j)] = 0

    return memo[(i, j)]



def main():

    T = stdin.readline().strip()

    R = T[::-1]

    memo = {}

    mejor = 0
    for i in range(len(T)):
        for j in range(len(T) - i):
            pos = len(T) - j - 1

            if i < pos:
                valor = phi(i, j, memo, T, R)
                mejor = max(mejor, valor)

    print(mejor)

main()