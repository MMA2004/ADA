"""
Mateo Monroy Aristizabal
14/03/2026

"""

from sys import stdin


def mejorTiempo(i, bolitasDisponibles, tiempos, bolitas, memo):

    if (i, bolitasDisponibles) in memo:
        ans = memo[(i, bolitasDisponibles)]
    else:

        if i == len(tiempos):
            ans = 0
            memo[(i, bolitasDisponibles)] = ans
        else:

            if bolitasDisponibles > 0:
                nuevasBolitasDisponibles = bolitasDisponibles + bolitas[i]
                nuevasBolitasDisponibles = min(nuevasBolitasDisponibles, len(tiempos))
                ans = min(mejorTiempo(i+1, nuevasBolitasDisponibles - 1, tiempos, bolitas, memo) + (tiempos[i]//2), mejorTiempo(i+1, nuevasBolitasDisponibles, tiempos, bolitas, memo) + tiempos[i])
                memo[(i, bolitasDisponibles)] = ans
            else:
                nuevasBolitasDisponibles = bolitasDisponibles + bolitas[i]
                nuevasBolitasDisponibles = min(nuevasBolitasDisponibles, len(tiempos))
                ans = mejorTiempo(i+1, nuevasBolitasDisponibles, tiempos, bolitas, memo) + tiempos[i]
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

        print(ans)

        rutas = int(stdin.readline())

main()