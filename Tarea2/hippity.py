from sys import stdin

def dp_busqueda(p, q, m, k, n, memo):
    # Si ya calculamos este estado, retornamos el valor guardado
    if memo[p][q] != -1:
        return memo[p][q]

    max_proximo = 0

    # Direcciones: Arriba, Abajo, Izquierda, Derecha
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dp, dq in direcciones:
        # Intentar saltar distancias desde 1 hasta k
        for d in range(1, k + 1):
            np, nq = p + dp * d, q + dq * d

            # Verificar límites de la matriz
            if 0 <= np < n and 0 <= nq < n:
                # Solo saltar si hay MÁS monedas que en la celda actual
                if m[np][nq] > m[p][q]:
                    max_proximo = max(max_proximo, dp_busqueda(np, nq, m, k, n, memo))

    memo[p][q] = m[p][q] + max_proximo
    return memo[p][q]


def main():
    casos = int(stdin.readline())

    for _ in range(casos):

        n, k = map(int, stdin.readline().split())

        matriz = [ [ 0 for _ in range(n) ] for _ in range(n) ]

        for i in range(n):
            lista = list(map(int, stdin.readline().split()))
            for j in range(n):
                matriz[i][j] = lista[j]


        print(dp_busqueda(0, 0, matriz, k, n, matriz))

main()
