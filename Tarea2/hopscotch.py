from sys import stdin
"""
def dp_busqueda(p, q, m, k, n, memo):

    # Si ya está calculado
    if (p, q) in memo:
        ans = memo[(p, q)]

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

    # Guardamos el resultado incluyendo las monedas actuales
    memo[(p, q)] = m[p][q] + max_proximo
    ans = memo[(p, q)]
    return ans
"""

def dp_busqueda(p, q, m, k, n, memo, profundidad=0):

    indent = "  " * profundidad

    print(f"{indent}Entrando a ({p},{q}) con {m[p][q]} monedas")

    # Si ya está calculado
    if (p, q) in memo:
        print(f"{indent}  -> Ya calculado: {memo[(p,q)]}")
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

                        print(f"{indent}  Intentando salto a ({np},{nq}) con {m[np][nq]} monedas")

                        candidato = dp_busqueda(np, nq, m, k, n, memo, profundidad+1)

                        print(f"{indent}  Regresando a ({p},{q}), candidato desde ({np},{nq}) = {candidato}")

                        max_proximo = max(max_proximo, candidato)

        memo[(p, q)] = m[p][q] + max_proximo
        ans = memo[(p, q)]

    print(f"{indent}Guardando en memo ({p},{q}) = {memo[(p,q)]}")
    print(f"{indent}Saliendo de ({p},{q})\n")

    return ans

def main():
    casos = int(stdin.readline())

    for c in range(casos):

        n, k = map(int, stdin.readline().split())

        matriz = []
        for _ in range(n):
            matriz.append(list(map(int, stdin.readline().split())))

        memo = {}  # ← ahora es diccionario

        resultado = dp_busqueda(0, 0, matriz, k, n, memo)
        print(memo)
        print(resultado)



main()
