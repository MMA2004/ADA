import sys

# Aumentar el límite de recursión
sys.setrecursionlimit(2000)
INF = float('inf')



# 2. La función DP con estructura clásica
def dp(u, idx, k, memo, graph, isTransmission):
    # Verificar si ya calculamos este estado
    if (u, idx, k) in memo:
        return memo[(u, idx, k)]

    # CASO BASE: Ya no hay más hijos para evaluar en este nodo
    if idx == len(graph[u]):
        k_propio = 1 if isTransmission[u] else 0
        if k == k_propio:
            ans = 0  # Cumplimos la meta de k exactos, no sumamos más aristas
        else:
            ans = -INF  # Estado inválido: sobraron o faltaron nodos por asignar
    else:
        v, w = graph[u][idx]
        ans = -INF

        # OPCIÓN 1: NO tomar la rama de este hijo
        # Le pasamos toda la responsabilidad de formar 'k' a los siguientes hijos
        ans = max(ans, dp(u, idx + 1, k, memo, graph, isTransmission))

        # OPCIÓN 2: TOMAR la rama de este hijo
        # Le damos 'k_v' nodos al hijo 'v', y 'k - k_v' a los siguientes hijos de 'u'
        # k_v debe ser al menos 1 porque para tomar la rama, el hijo debe infectarse
        for k_v in range(1, k + 1):
            val_hijo = dp(v, 0, k_v, memo, graph, isTransmission)  # Lo que gana el hijo usando todos sus propios hijos
            val_resto = dp(u, idx + 1, k - k_v, memo, graph, isTransmission)  # Lo que ganan los demás hijos de u

            if val_hijo != -INF and val_resto != -INF:
                ans = max(ans, val_hijo + val_resto + w)

    # Guardar en memoria
    memo[(u, idx, k)] = ans
    return ans

def main():
    line1 = sys.stdin.readline().split()
    if not line1: return
    n, m, q = map(int, line1)

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))

    isTransmission = [False] * n
    for i in map(int, sys.stdin.readline().split()):
        isTransmission[i] = True

    lista_de_consultas = list(map(int, sys.stdin.readline().split()))

    # Memoria global para la DP
    memo = {}

    # 3. Procesar las consultas
    results = []
    for x in lista_de_consultas:
        if x == 0:
            results.append("0")
            continue

        max_cripto = 0
        # El ataque puede tener como "raíz" a cualquier nodo del árbol
        for u in range(n):
            if isTransmission[u]:
                val = dp(u, 0, x, memo, graph, isTransmission)
                print(u,val)
                if val > max_cripto:
                    max_cripto = val

        results.append(str(max_cripto))

    sys.stdout.write("\n".join(results) + "\n")



main()