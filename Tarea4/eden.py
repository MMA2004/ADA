"""
Mateo Monroy Aristizabal
8987333
22/04/2026
"""


from sys import stdin


def checkFinal(sol, automata, estado):
    # verificar posición 0
    ans = False
    a = sol[-1]
    b = sol[0]
    c = sol[1]
    num = (a << 2) | (b << 1) | c

    if automata[7 - num] == estado[0]:
        # verificar última posición
        a = sol[-2]
        b = sol[-1]
        c = sol[0]
        num = (a << 2) | (b << 1) | c

        if automata[7 - num] == estado[-1]:
            ans = True

    return ans

def check(sol, automata, estado):
    a = sol[-3]
    b = sol[-2]
    c = sol[-1]
    num = a << 2 | b << 1 | c
    return automata[7 - num] == estado[len(sol) - 2]


def phi(sol, estado, automata, t):
    ans = False

    if len(sol) == t:
        ans = checkFinal(sol, automata, estado)
    else:
        i = 0
        opciones = [0, 1]

        while not ans and i < 2:
            bit = opciones[i]
            sol.append(bit)

            if len(sol) < 3 or check(sol, automata, estado):
                ans = phi(sol, estado, automata, t)

            sol.pop()
            i += 1

    return ans


def main():
    linea = stdin.readline()
    while linea:
        id, n, estado = linea.split()

        id = int(id)
        n = int(n)
        estado = list(map(int, estado))

        automata = list(map(int, format(id, '08b')))

        if phi([], estado, automata, n):
            print("REACHABLE")
        else:
            print("GARDEN OF EDEN")

        linea = stdin.readline()


main()

