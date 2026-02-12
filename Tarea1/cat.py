"""
H: Altura del gato inicial (dada).
W: Número de gatos trabajadores (de altura 1, dado).
N: Número de gatos dentro de cada sombrero (desconocido).
k: El número de niveles de gatos (cuántas veces "abrimos" un sombrero).

La Altura disminuye: Cada nivel de gatos mide 1/N+1 de la altura del gato anterior.
Si empezamos en H y llegamos a altura 1 en k pasos, tenemos:
                        H = (N+1)^k

La Cantidad aumenta: Cada gato tiene N gatos en su sombrero.
Después de k niveles, el número de trabajadores (gatos de altura 1) es:
                        W = N^k

Encontrar N y k

Sabemos que H = (N+1)^k y W = N^k.
Esto implica que: (N+1) = H^(1/k) y N = W^(1/k)

Por lo tanto:
H^(1/k) = W^(1/k) + 1

H^(1/k) - W^(1/k) = 1

Sabemos que después de k niveles, partiendo de una altura inicial H, llegamos a la altura del trabajador (que es 1):
1 = H/(N+1)^k
H = (N+1)^k

Para maximizar el exponente k, necesitamos que la base (N+1) sea lo más pequeña posible.
Como vimos, el valor mínimo de N+1 es 2.
H >= 2^k

Aplicando logaritmos en base 2 a ambos lados:

log2 H >= log2(2^k)
log2 H >= k
"""

from sys import stdin

import math

def buscar_k(l, r, H, W):
    if r - l == 1:
        ans = l

    else:
        mid_k = (l + r) // 2

        if H ** (1 / mid_k) - W ** (1 / mid_k) < 1:
            ans = buscar_k(l, mid_k, H, W)

        else:
            ans = buscar_k(mid_k, r, H, W)

    return ans


def main():
    H, W = map(int, stdin.readline().split())

    while H != 0 and W != 0:

        k = buscar_k(1, math.log(H, 2), H, W)

        N = W ** (1 / k)

        gatos_vagos = 0
        for i in range(int(k)):  # Esto va de 0 a k-1
            gatos_vagos += N ** i

        altura_total = 0
        cantidad_gatos = 1  # Empezamos con el gato inicial (N^0)
        altura_del_gato = H  # Altura del gato inicial

        for i in range(int(k) + 1):  # Incluye el nivel k (los trabajadores)
            altura_total += cantidad_gatos * altura_del_gato

            # Preparamos los valores para el siguiente nivel
            cantidad_gatos *= N
            altura_del_gato //= (N + 1)  # División entera para mantener precisión

        print(int(round(gatos_vagos)), int(round(altura_total)))


        H, W = map(int, stdin.readline().split())



main()