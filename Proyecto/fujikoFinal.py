"""
Mateo Monroy Aristizabal
8987333

Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

INF = float('inf')


def count_transmission_nodes(u, graph, is_transmission, sub_count):
    """
    Cuenta recursivamente cuántos nodos de transmisión hay en el subárbol
    de u (incluyendo u mismo si es de transmisión) y almacena el resultado
    en sub_count[u].

    Args:
        u (int): El nodo raíz del subárbol a evaluar.
        graph (list): Lista de adyacencia. graph[u] contiene tuplas (v, w).
        is_transmission (list): Lista de booleanos que indica si cada nodo
            es de transmisión.
        sub_count (list): Lista donde se almacena el conteo de cada nodo.
            Debe inicializarse con ceros antes de la primera llamada.
    """
    sub_count[u] = 1 if is_transmission[u] else 0
    for v, w in graph[u]:
        count_transmission_nodes(v, graph, is_transmission, sub_count)
        sub_count[u] += sub_count[v]



def phi(u, idx, k, memo, graph, is_transmission, sub_count):
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
            is_transmission (list): Estructura que mapea el ID de un nodo a un
                booleano, indicando si dicho nodo es de transmisión (`True`) o no (`False`)
            sub_count (list): Lista donde sub_count[u] indica cuántos nodos de transmisión
                hay en el subárbol de u (incluyendo u mismo). Se usa para podar ramas
                que no pueden aportar suficientes nodos de transmisión.

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
            k_propio = 1 if is_transmission[u] else 0
            if k == k_propio:
                ans = 0  # Cumplimos la meta de k exactos, no sumamos más aristas
            else:
                ans = -INF  # Estado inválido: sobraron o faltaron nodos por asignar
        else:
            v, w = graph[u][idx]

            # OPCIÓN 1: NO tomar la rama de este hijo
            # Le pasamos toda la responsabilidad de formar 'k' a los siguientes hijos
            ans = phi(u, idx + 1, k, memo, graph, is_transmission, sub_count)

            # OPCIÓN 2: TOMAR la rama de este hijo
            # Le damos 'k_v' nodos al hijo 'v', y 'k - k_v' a los siguientes hijos de 'u'
            # k_v debe ser al menos 1 porque para tomar la rama, el hijo debe infectarse
            for k_v in range(1, k + 1):
                # PODA: si el subárbol del hijo v tiene al menos k_v nodos de transmisión
                # entonces tiene sentido explorar esta rama
                if sub_count[v] >= k_v:
                    val_son = phi(v, 0, k_v, memo, graph, is_transmission, sub_count)  # Lo que gana el hijo usando todos sus propios hijos
                    val_rest = phi(u, idx + 1, k - k_v, memo, graph, is_transmission, sub_count)  # Lo que ganan los demás hijos de u

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
        has_parent = [False] * n
        for _ in range(n - 1):
            u, v, w = map(int, stdin.readline().split())
            graph[u].append((v, w))
            has_parent[v] = True

        is_transmission = [False] * n
        for i in map(int, stdin.readline().split()):
            is_transmission[i] = True

        query_list = list(map(int, stdin.readline().split()))

        # Encontrar la raíz del árbol
        root = 0
        i = 0
        found = False

        while not found and i < n:
            if not has_parent[i]:
                root = i
                found = True
            i += 1

        # Precalcular cuántos nodos de transmisión hay en cada subárbol
        sub_count = [0] * n
        count_transmission_nodes(root, graph, is_transmission, sub_count)

        # Memoria global para la DP
        memo = {}

        for k in query_list:
            max_cripto = 0
            if k != 0:
                # El ataque puede tener como "raíz" a cualquier nodo del árbol si es de transmisión
                for u in range(n):
                    # PODA: solo llamar a phi si el nodo es de transmisión y su subárbol
                    # tiene al menos k nodos de transmisión
                    if is_transmission[u] and sub_count[u] >= k:
                        val = phi(u, 0, k, memo, graph, is_transmission, sub_count)
                        if val > max_cripto:
                            max_cripto = val

            print(max_cripto)

        line = stdin.readline().split()



main()
