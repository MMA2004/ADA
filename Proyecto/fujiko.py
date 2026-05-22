"""
Mateo Monroy Aristizabal
8987333

"""
from sys import stdin

INF = float('inf')


def phi(u, idx, k, memo, graph, isTransmission):
    """
        Calcula mediante programación dinámica el peso máximo posible
        de las aristas conectadas en el subárbol del nodo `u`, de modo que se
        incluyan exactamente `k` nodos de transmisión.

        Args:
            u (int): El identificador del nodo actual que se está evaluando.
            idx (int): El índice del hijo actual del nodo `u` dentro de la lista de adyacencia.
            k (int): La cantidad exacta de nodos de transmisión que deben incluirse
                (asignarse) en el subárbol a partir de este punto.
            memo (dict): Diccionario utilizado para la memorización. Las claves son
                tuplas de estado `(u, idx, k)` y los valores son los pesos máximos calculados.
            graph (list): Lista de adyacencia que representa el árbol.
                `graph[u]` contiene una lista de tuplas `(v, w)`, donde `v` es el nodo hijo
                y `w` es el peso de la arista que los conecta.
            isTransmission (list): Estructura que mapea el ID de un nodo a un
                booleano, indicando si dicho nodo es de transmisión (`True`) o no (`False`).

        Returns:
            int: El peso máximo acumulado de las aristas si es posible alcanzar
            exactamente `k` nodos de transmisión. Retorna `-INF` si el estado es inválido
            (no es posible formar exactamente `k` nodos).
        """
    # Verificar si ya calculamos este estado
    if (u, idx, k) in memo:
        ans = memo[(u, idx, k)]
    else:
        # CASO BASE: Ya no hay más hijos para evaluar en este nodo
        if idx == len(graph[u]):
            k_propio = 1 if isTransmission[u] else 0
            if k == k_propio:
                ans = 0  # Cumplimos la meta de k exactos, no sumamos más aristas
            else:
                ans = -INF  # Estado inválido: sobraron o faltaron nodos por asignar
        else:
            v, w = graph[u][idx]

            # OPCIÓN 1: NO tomar la rama de este hijo
            # Le pasamos toda la responsabilidad de formar 'k' a los siguientes hijos
            ans = phi(u, idx + 1, k, memo, graph, isTransmission)

            # OPCIÓN 2: TOMAR la rama de este hijo
            # Le damos 'k_v' nodos al hijo 'v', y 'k - k_v' a los siguientes hijos de 'u'
            # k_v debe ser al menos 1 porque para tomar la rama, el hijo debe infectarse
            for k_v in range(1, k + 1):
                val_son = phi(v, 0, k_v, memo, graph, isTransmission)  # Lo que gana el hijo usando todos sus propios hijos
                val_rest = phi(u, idx + 1, k - k_v, memo, graph, isTransmission)  # Lo que ganan los demás hijos de u

                if val_son != -INF and val_rest != -INF:
                    ans = max(ans, val_son + val_rest + w)

    # Guardar en memoria
    memo[(u, idx, k)] = ans
    return ans

def main():
    """
        Función principal que maneja la lectura de datos, construcción del grafo
        y la ejecución de las consultas.

        Lee desde la entrada múltiples casos de prueba. Para cada caso,
        construye un árbol (n-1 aristas), identifica los nodos de transmisión y responde a
        múltiples consultas usando programación dinámica. Para cada consulta 'k',
        busca el peso máximo posible de un subárbol que contenga exactamente 'k' nodos
        de transmisión.

        Formato de entrada esperado por caso de prueba:
            - Línea 1: Tres enteros `n` (nodos), `m` (nodos de transmisión), `q` (consultas).
            - Siguientes `n-1` líneas: Tres enteros `u v w` (arista de `u` a `v` con peso `w`).
            - Siguiente línea: `m` enteros que representan los IDs de los nodos de transmisión.
            - Siguiente línea: `q` enteros que representan los valores de `k` a consultar.

        Returns:
            None. Los resultados de cada consulta se imprimen directamente en la
            salida.
        """
    line = stdin.readline().split()
    while line:
        n, m, q = map(int, line)

        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v, w = map(int, stdin.readline().split())
            graph[u].append((v, w))

        isTransmission = [False] * n
        for i in map(int, stdin.readline().split()):
            isTransmission[i] = True

        query_list = list(map(int, stdin.readline().split()))

        # Memoria global para la DP
        memo = {}

        # 3. Procesar las consultas
        results = []
        for k in query_list:
            max_cripto = 0
            if k == 0:
                results.append("0")
            else:
                # El ataque puede tener como "raíz" a cualquier nodo del árbol
                for u in range(n):
                    if isTransmission[u]:
                        val = phi(u, 0, k, memo, graph, isTransmission)
                        if val > max_cripto:
                            max_cripto = val

            print(max_cripto)

        line = stdin.readline().split()



main()