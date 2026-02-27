"""
Mateo Monroy Aristizabal
8987333
17/02/2024

Complejidad:

La funcion merge tiene una complejidad de O(n) ya que recorre todo el arreglo de los oponentes.

La funcion buscar_k es una biseccion recursiva que se va dividiendo en 3 mitades
parecido a una busqueda ternaria.

su complejidad es:
m = es la distacia total de la carrera

T(m) = T(2m/3) + O(n)

No se puede aplicar el teorema maestro porque hay dos variables diferentes en la ecuacion.

"""

from sys import stdin

def margen(t, r, tramposo_running, tramposo_cycling, oponentes):
    k = t - r
    # Tiempo del tramposo: T = r/v_r + k/v_k
    tiempo_tramposo = (r / tramposo_running) + (k / tramposo_cycling)

    # Buscar al oponente más rápido para esta r específica
    # (El que tenga el tiempo mínimo)
    mejor_oponenten = float('inf')
    for oponenten_running, oponenten_cycling in oponentes:
        t_oponenten = (r / oponenten_running) + (k / oponenten_cycling)
        if t_oponenten < mejor_oponenten:
            mejor_oponenten = t_oponenten

    # El margen en segundos es (T_oponente - T_tramposo) * 3600
    return (mejor_oponenten - tiempo_tramposo) * 3600


def buscar_r(l, r, t, tramposo_running, tramposo_cycling, oponentes):
    if (r - l) < 0.000001:
        ans = l

    else:

        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3

        if margen(t, m1, tramposo_running, tramposo_cycling, oponentes) < margen(t, m2, tramposo_running, tramposo_cycling, oponentes):
            ans = buscar_r(m1, r, t, tramposo_running, tramposo_cycling, oponentes)
        else:
            ans = buscar_r(l, m2, t, tramposo_running, tramposo_cycling, oponentes)

    return ans

def main():



    t = stdin.readline()

    while t != "":
        if t != "\n":

            t = int(t)

            n = int(stdin.readline())

            velocidades = []
            for _ in range(n):
                running, cycling = map(float, stdin.readline().split())
                velocidades.append((running, cycling))

            tramposo_running, tramposo_cycling = velocidades[-1]
            oponentes = velocidades[:-1]

            mejor_running = buscar_r(0, t, t, tramposo_running, tramposo_cycling, oponentes)

            max_margen = margen(t, mejor_running, tramposo_running, tramposo_cycling, oponentes)

            if max_margen > 0:

                print(f"The cheater can win by {round(max_margen)} seconds with r = {mejor_running:.2f}km and k = {t - mejor_running:.2f}km.")

            elif max_margen < 0:

                print("The cheater cannot win.")

            else:
                print("0")



        t = stdin.readline()



main()