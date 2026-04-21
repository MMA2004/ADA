from sys import stdin

def ordenada(sol):
    return sol == sorted(sol)

def phi1(sol, swaps, visitados):
    global mejor, contador

    if swaps <= mejor:

        if ordenada(sol):
            if swaps < mejor:
                mejor = swaps
                contador = 1
            elif swaps == mejor:
                contador += 1

        else:
            for i in range(len(sol) - 1):
                sol[i], sol[i + 1] = sol[i + 1], sol[i]

                nuevo_estado = tuple(sol)
                if nuevo_estado not in visitados:
                    visitados.add(nuevo_estado)
                    phi(sol, swaps + 1, visitados)
                    visitados.remove(nuevo_estado)

                sol[i], sol[i + 1] = sol[i + 1], sol[i]\



def phi(sol, swaps, anterior):
    global mejor, contador

    if swaps <= mejor:

        if ordenada(sol):
            if swaps < mejor:
                mejor = swaps
                contador = 1
            elif swaps == mejor:
                contador += 1

        else:
            for i in range(len(sol) - 1):
                sol[i], sol[i + 1] = sol[i + 1], sol[i]


                if anterior != i:

                    phi(sol, swaps + 1, i)


                sol[i], sol[i + 1] = sol[i + 1], sol[i]




def main():

    linea = stdin.readline()
    caso = 0
    while linea.strip() != "0":
        global mejor, contador

        sol = list(map(int, linea.split()))
        sol.pop(0)
        contador = 0
        #visitados = {tuple(sol)}
        anterior = -1
        swaps = 0
        mejor = float('inf')
        if not ordenada(sol):
            phi(sol, swaps, anterior)

        print(f"There are {contador} swap maps for input data set {caso + 1}")
        caso += 1

        linea = stdin.readline()

main()


