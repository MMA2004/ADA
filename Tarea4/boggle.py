from sys import stdin

direcciones = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def criterio(palabra):
    return (len(palabra), palabra)

def phi(sol, matriz, visitados, i, j):
    global res

    if not sol or matriz[i][j] > sol[-1]:

        sol.append(matriz[i][j])

        visitados[i][j] = True

        if len(sol) >= 3:
            res.add("".join(sol))

        for k in direcciones:
            x, y = i + k[0], j + k[1]

            if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]):

                if not visitados[x][y]:
                    phi(sol, matriz, visitados, x, y)

        sol.pop()
        visitados[i][j] = False



def main():
    casos = int(stdin.readline())
    global res
    for i in range(casos):
        n = int(stdin.readline())
        matriz = []
        visitados = [[False] * n for _ in range(n)]
        res = set()
        for j in range(n):
            linea = stdin.readline().strip()
            matriz.append(list(linea))

        for x in range(n):
            for y in range(n):
                phi([], matriz, visitados, x, y)

        resultado = list(res)
        resultado.sort(key=criterio)
        print(resultado)

main()







