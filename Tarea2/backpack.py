"""
Mateo Monroy Aristizabal
14/03/2026

Compeljidad:

la funcion simularViaje es O(N) donde N es el numero de distancias entre campamentos.

la funcion buscar es T(n) = t(n/2) + O(N)

porque en cada recursion parte la entrada a la mitad y descarta una mitad.
y por cada llamado recursivo se ejecuta simularViaje.

en este caso no se puede aplicar el teorema maestro ya que simularViaje siempre recorre todo el arreglo de distancias
que tiene tamano N y no se va reduciendo en ningun momento.

"""

from sys import stdin



def simularViaje(distancia_por_dia, distancias, k):

    noches_usadas = 0
    distancia_caminada = 0

    for d in distancias:

        if distancia_por_dia >= distancia_caminada + d:
            distancia_caminada += d
        else:
            noches_usadas += 1
            distancia_caminada = d

    return noches_usadas <= k



def buscar(l, r, distancias, k):

    if l == r:
        ans = l
    else:

        mid = (l + r) // 2

        if simularViaje(mid, distancias, k):
            ans = buscar(l, mid, distancias, k)
        else:
            ans = buscar(mid + 1, r, distancias, k)

    return ans


def main():


    linea = stdin.readline()

    while linea:
        N, K = map(int, linea.split())

        distancias = []
        sumDistancias = 0
        maxDistancia = 0
        for i in range(N + 1):
            distancias.append(int(stdin.readline()))
            sumDistancias += distancias[i]
            maxDistancia = max(maxDistancia, distancias[i])


        ans = buscar(maxDistancia, sumDistancias, distancias, K)

        print(ans)

        linea = stdin.readline()


main()