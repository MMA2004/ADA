import sys

# Aumentar el límite de recursión
sys.setrecursionlimit(2000)
INF = float('inf')


def precalcular_transmisiones(u, graph, isTransmission, sub_tree_trans):
    # Contamos 1 si el nodo actual 'u' es de transmisión
    conteo = 1 if isTransmission[u] else 0

    # Sumamos recursivamente lo que aporten sus hijos
    for v, _ in graph[u]:
        conteo += precalcular_transmisiones(v, graph, isTransmission, sub_tree_trans)

    sub_tree_trans[u] = conteo
    return conteo

# 2. La función DP con estructura clásica
def dp(u, idx, k, memo, graph, isTransmission):
    # Verificar si ya calculamos este estado
    if (u, idx, k) in memo:
        print("si", memo[(u, idx, k)])
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


def dp1(u, idx, k, memo, graph, isTransmission, sub_tree_trans, sufijos_trans):
    # PODA 1: Si pides más de lo que el nodo completo puede ofrecer, aborta inmediatamente
    if k > sub_tree_trans[u]:
        return -INF

    # Verificar si ya calculamos este estado
    if (u, idx, k) in memo:
        print("si")
        return memo[(u, idx, k)]

    # CASO BASE: Ya no hay más hijos para evaluar en este nodo
    if idx == len(graph[u]):
        k_propio = 1 if isTransmission[u] else 0
        if k == k_propio:
            ans = 0
        else:
            ans = -INF
    else:
        v, w = graph[u][idx]
        ans = -INF

        # OPCIÓN 1: NO tomar la rama de este hijo
        # PODA 2: Solo pasamos el 'k' al resto si los hijos que quedan son suficientes
        if k <= sufijos_trans[u][idx + 1]:
            ans = max(ans, dp1(u, idx + 1, k, memo, graph, isTransmission, sub_tree_trans, sufijos_trans))

        ## OPCIÓN 2: TOMAR la rama de este hijo
        # PODA 3: El hijo 'v' no puede recibir más de lo que tiene su subárbol
        limite_max_hijo = min(k, sub_tree_trans[v])

        # NUEVA OPTIMIZACIÓN: El hijo 'v' debe recibir lo suficiente para que el resto no se quede corto
        # Si (k - disponibles_resto) es mayor a 1, nos saltamos todos los k_v inválidos desde el inicio
        disponibles_resto = sufijos_trans[u][idx + 1]
        limite_min_hijo = max(1, k - disponibles_resto)

        for k_v in range(limite_min_hijo, limite_max_hijo + 1):
            k_restante = k - k_v

            val_hijo = dp(v, 0, k_v, memo, graph, isTransmission, sub_tree_trans, sufijos_trans)
            val_resto = dp(u, idx + 1, k_restante, memo, graph, isTransmission, sub_tree_trans, sufijos_trans)

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

    # 1. Correr el precalculo normal
    sub_tree_trans = [0] * n
    precalcular_transmisiones(0, graph, isTransmission, sub_tree_trans)

    # 2. Crear los sufijos para cada nodo u
    sufijos_trans = [[] for _ in range(n)]
    for u in range(n):
        num_hijos = len(graph[u])
        # Inicializamos el arreglo de sufijos con ceros (un espacio extra para el caso base)
        sufijos = [0] * (num_hijos + 1)

        # El valor propio del nodo se le asigna a la última posición de control (caso base)
        sufijos[num_hijos] = 1 if isTransmission[u] else 0

        # Acumulamos de atrás hacia adelante
        for i in range(num_hijos - 1, -1, -1):
            v, _ = graph[u][i]
            sufijos[i] = sub_tree_trans[v] + sufijos[i + 1]

        sufijos_trans[u] = sufijos

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