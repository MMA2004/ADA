from sys import stdin

def phi(sol, estado, automata):
    print(sol)




def main():
    claves = ["111", "110", "101", "100", "011", "010", "001", "000"]



    id, n, estado = stdin.readline().split()

    id = int(id)
    n = int(n)
    estado = list(estado)

    regla = format(id, '08b')
    automata = {}

    for i in range(8):
        automata[claves[i]] = int(regla[i])

    print(automata)






main()

