"""
Mateo Monroy Aristizabal
8987333
02/04/2026

Complejidad:

Primero se realiza un ordenamiento de los números con los que se realizará el cálculo.
Esto tiene un costo de O(n log n), donde n es la cantidad de números.

Luego se ejecuta la función calcular_signos, que recorre toda la expresión
para determinar el signo de cada variable 'x'. Esta operación tiene un costo
de O(m), donde m es la longitud de la expresión.

Posteriormente, se ejecuta la función maximo_calculo, que recorre la lista
de signos y asigna los valores correspondientes. Esto tiene un costo de O(n),
donde n es la cantidad de variables 'x'.

Por lo tanto, la complejidad total del algoritmo es:

O(n log n + m + n)

Por lo tanto:
O(n log n)
"""

from sys import stdin


def maximo_calculo(numeros, N, signos):
    ans = 0
    l, r = 0, N - 1

    for s in signos:
        if s == 1:
            ans += numeros[r]
            r -= 1
        else:
            ans -= numeros[l]
            l += 1

    return ans


def calcular_signos(expresion):

    signos = []
    signo_del_parentesis = [1]
    signo_actual = 1

    for simbolo in expresion:
        if simbolo == 'x':
            signos.append(signo_actual)
        elif simbolo == '+':
            signo_actual = signo_del_parentesis[-1]
        elif simbolo == '-':
            signo_actual= -(signo_del_parentesis[-1])
        elif simbolo == '(':
            signo_del_parentesis.append(signo_actual)
        elif simbolo == ')':
            signo_del_parentesis.pop()
            signo_actual = signo_del_parentesis[-1]

    return signos


def main():
    casos = int(stdin.readline())

    while casos:

        expresion = stdin.readline().strip()

        N = int(stdin.readline())

        numeros = list(map(int, stdin.readline().split()))

        numeros.sort()

        signos = calcular_signos(expresion)

        print(maximo_calculo(numeros, N, signos))
        casos -= 1


main()