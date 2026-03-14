from sys import stdin


def mejorTiempo(i, bolitasDisponibles, tiempos, bolitas, memo):

    if (i, bolitasDisponibles) in memo:
        ans = memo[(i, bolitasDisponibles)]
    else:

        if i == len(tiempos):
            ans = 0

        else:

            if bolitasDisponibles > 0:
                bolitasDisponibles += bolitas[i]
                ans = min(mejorTiempo(i+1, bolitasDisponibles - 1, tiempos, bolitas, memo) + (tiempos[i]/2), mejorTiempo(i+1, bolitasDisponibles, tiempos, bolitas, memo) + tiempos[i])

            else:
                bolitasDisponibles += bolitas[i]
                ans = mejorTiempo(i+1, bolitasDisponibles, tiempos, bolitas, memo) + tiempos[i]

    memo[(i, bolitasDisponibles)] = ans
    return ans


def main():
    rutas = int(stdin.readline())

    while rutas != 0:

        tiempos = []
        bolitas = []

        for i in range(rutas):
            t, b = map(int, stdin.readline().split())
            tiempos.append(t)
            bolitas.append(b)

        memo = {}

        ans = mejorTiempo(0, 0, tiempos, bolitas, memo)

        print(int(ans))

        rutas = int(stdin.readline())

main()