def phi(i, n, count):
    # Si en cualquier punto el contador es negativo, ya no es válido
    if count < 0:
        return -1  # Usamos -1 como indicador de error

    # Caso base: llegamos al final
    if i == len(n):
        return count

    # Procesamos el carácter actual y pasamos el nuevo count a la siguiente llamada
    if n[i] == "(":
        return phi(i + 1, n, count + 1)
    elif n[i] == ")":
        return phi(i + 1, n, count - 1)
    else:
        return phi(i + 1, n, count)


def main():
    n = "()()"  # Ejemplo de cadena desbalanceada que suma cero al final
    ans = phi(0, n, 0)

    if ans == 0:
        print("Balanceado")
    else:
        print("No balanceado o inválido")


main()