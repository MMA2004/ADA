from sys import stdin

def ordenada(sol):
    return sol == sorted(sol)

def phi(sol, swaps, visitados):
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
                    sol[i], sol[i + 1] = sol[i + 1], sol[i]

def phi2(sol, swaps, objetivo):
    global mejor, contador, dist

    estado = tuple(sol)

    if estado not in dist or swaps <= dist[estado]:
        dist[estado] = swaps

        if swaps <= mejor:

            if estado == objetivo:
                if swaps < mejor:
                    mejor = swaps
                    contador = 1
                elif swaps == mejor:
                    contador += 1

            else:
                i = 0
                while i < len(sol) - 1:

                    sol[i], sol[i + 1] = sol[i + 1], sol[i]

                    phi2(sol, swaps + 1, objetivo)

                    sol[i], sol[i + 1] = sol[i + 1], sol[i]

                    i += 1



def phi(sol, swaps):
    global mejor, contador, objetivo, dist

    estado = tuple(sol)

    # 🔥 poda por mejor conocido
    if estado in dist and dist[estado] <= swaps:
        return
    dist[estado] = swaps

    # 🔥 poda por profundidad
    if swaps > mejor:
        return

    # 🎯 solución
    if estado == objetivo:
        if swaps < mejor:
            mejor = swaps
            contador = 1
        elif swaps == mejor:
            contador += 1
        return

    # explorar swaps
    for i in range(len(sol) - 1):
        sol[i], sol[i+1] = sol[i+1], sol[i]

        phi(sol, swaps + 1)

        sol[i], sol[i+1] = sol[i+1], sol[i]




def main():

    linea = stdin.readline()
    caso = 0
    while linea.strip() != "0":
        global mejor, contador, dist

        sol = list(map(int, linea.split()))
        sol.pop(0)
        objetivo = tuple(sorted(sol))
        mejor = float('inf')
        contador = 0
        dist = {}
        visitados = {tuple(sol)}



        if not ordenada(sol):
            phi2(sol, 0, objetivo)

        print(f"There are {contador} swap maps for input data set {caso + 1}")
        caso += 1

        linea = stdin.readline()

main()


