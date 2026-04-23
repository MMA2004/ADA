"""
Mateo Monroy Aristizabal
8987333
22/04/2026
"""

from sys import stdin

def phi(sol, swaps, objetivo, anterior):
    global mejor, contador


    if swaps <= mejor:

        if sol == objetivo:
            if swaps < mejor:
                mejor = swaps
                contador = 1
            elif swaps == mejor:
                contador += 1

        else:
            i = 0
            while i < len(sol) - 1:

                if i != anterior:
                    if sol[i] > sol[i + 1]:

                        sol[i], sol[i + 1] = sol[i + 1], sol[i]

                        phi(sol, swaps + 1, objetivo, i)

                        sol[i], sol[i + 1] = sol[i + 1], sol[i]

                i += 1


def main():

    linea = stdin.readline()
    caso = 0
    while linea.strip() != "0":
        global mejor, contador

        sol = list(map(int, linea.split()))
        sol.pop(0)
        objetivo = sorted(sol)
        mejor = float('inf')
        contador = 0
        if sol != objetivo:
            phi(sol, 0, objetivo, -1)

        print(f"There are {contador} swap maps for input data set {caso + 1}.")
        caso += 1

        linea = stdin.readline()

main()


