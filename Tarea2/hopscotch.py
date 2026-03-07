"""
Mateo Monroy Aristizabal
05/03/2026

Complejidad:
La memoización usa como clave (p, q), que representa una celda del tablero.
El tablero es de tamaño: n * n
Por lo tanto, el número máximo de estados distintos que puede calcular la función es: O(n²)

Dentro de cada llamada:
Hay 4 direcciones posibles.
Se pueden explorar k saltos en cada dirección.
Entonces el número máximo de iteraciones es: 4 * k

En cada iteración solo se hacen operaciones O(1) y posiblemente una llamada recursiva (que no se vuelve a recalcular por el memo).

Por lo tanto, el costo por estado es: O(k)

Complejidad temporal:

O(n² * k)

Osea O(n²)

omplejidad espacial:

memo guarda a lo sumo n² estados
O(n²)
"""

from sys import stdin

def dp_busqueda(p, q, m, k, n, memo):

    # Si ya está calculado
    if (p, q) in memo:
        ans = memo[(p, q)]
    else:
        max_proximo = 0
        direcciones = [(0,1), (0,-1), (1,0), (-1,0)]

        for dp, dq in direcciones:
            for d in range(1, k + 1):

                np = p + dp * d
                nq = q + dq * d

                if 0 <= np < n and 0 <= nq < n:
                    if m[np][nq] > m[p][q]:

                        candidato = dp_busqueda(np, nq, m, k, n, memo)

                        max_proximo = max(max_proximo, candidato)

        memo[(p, q)] = m[p][q] + max_proximo
        ans = memo[(p, q)]

    return ans

def main():
    casos = int(stdin.readline())

    for c in range(casos):
        stdin.readline()
        n, k = map(int, stdin.readline().split())

        matriz = []
        for _ in range(n):
            matriz.append(list(map(int, stdin.readline().split())))

        memo = {}

        resultado = dp_busqueda(0, 0, matriz, k, n, memo)

        if c != casos-1:
            print(f"{resultado}\n")
        else:
            print(resultado)


main()
