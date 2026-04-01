from sys import stdin


def calculo(expresion, numeros, N):

    signos = []
    stack = [1]  # pila de signos
    signo = 1

    for simbolo in expresion:
        if simbolo == 'x':
            signos.append(signo)
        elif simbolo == '+':
            signo = stack[-1]
        elif simbolo == '-':
            signo = -stack[-1]
        elif simbolo == '(':
            stack.append(signo)
        elif simbolo == ')':
            stack.pop()
            signo = stack[-1]

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


def main():
    casos = int(stdin.readline())

    while casos:

        expresion = stdin.readline().strip()

        N = int(stdin.readline())

        numeros = list(map(int, stdin.readline().split()))

        numeros.sort()

        print(calculo(expresion, numeros, N))
        casos -= 1


main()