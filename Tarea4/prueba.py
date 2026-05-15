"""
Nombre: César Zuluaga
Codigo: 8989815

"""

from sys import stdin

lago = []
checks = []
puntos_clave = []
movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
parejas_clave = {}
t = 0
ans = 0


def revision(x, y, mom_c):
    ans = True
    for i in range(mom_c, 3):
        ans = (x, y) != (puntos_clave[i])
    return ans


def revision1(n_x, n_y):
    return n_x >= 0 and n_x < len(lago) and n_y >= 0 and n_y < len(lago[n_x]) and lago[n_x][n_y] == False


def revision1_1(n_x, n_y):
    return n_x >= 0 and n_x < len(lago) and n_y >= 0 and n_y < len(lago[n_x])


def revision2(mom_c, vis, x, y):
    return mom_c < len(checks) and vis == checks[mom_c] and (x, y) == puntos_clave[mom_c]


def revision3(mom_c, vis):
    return mom_c < len(checks) and vis < checks[mom_c]


def revision4(mom_c, x, y, vis):
    ans = True
    if mom_c == 3:
        dist = (x) + abs(y - 1)
        if vis + dist > t:
            ans = False
    else:
        dist = abs(x - puntos_clave[mom_c][0]) + abs(y - puntos_clave[mom_c][1])
        if vis + dist > checks[mom_c]:
            ans = False
    return ans


def revision5(x, y):
    Ux, Uy = x + 1, y
    Rx, Ry = x, y + 1
    Dx, Dy = x - 1, y
    Lx, Ly = x, y - 1
    ans = True
    if revision1_1(Ux, Uy) and revision1_1(Rx, Ry) and revision1_1(Dx, Dy) and revision1_1(Lx, Ly):
        if lago[Ux][Uy] == False and lago[Dx][Dy] == False and lago[Rx][Ry] == True and lago[Lx][Ly] == True:
            ans = False

        elif lago[Ux][Uy] == True and lago[Dx][Dy] == True and lago[Rx][Ry] == False and lago[Lx][Ly] == False:
            ans = False

    return ans


def revision6(x, y):
    Ux, Uy = x + 1, y
    Rx, Ry = x, y + 1
    Dx, Dy = x - 1, y
    Lx, Ly = x, y - 1
    ans = True

    if (revision1_1(Ux, Uy) or revision1_1(Dx, Dy)) and revision1_1(Rx, Ry) and revision1_1(Lx, Ly):
        if lago[Rx][Ry] == True and lago[Lx][Ly] == True:
            if revision1_1(Ux, Uy) and lago[Ux][Uy] == False:
                ans = False
            if revision1_1(Dx, Dy) and lago[Dx][Dy] == False:
                ans = False

    elif (revision1_1(Lx, Ly) or revision1_1(Rx, Ry)) and revision1_1(Ux, Uy) and revision1_1(Dx, Dy):
        if lago[Ux][Uy] == True and lago[Dx][Dy] == True:
            if revision1_1(Rx, Ry) and lago[Rx][Ry] == False:
                ans = False
            if revision1_1(Lx, Ly) and lago[Lx][Ly] == False:
                ans = False
    return ans


def ice(x, y, vis, mom_c):
    global t
    global ans
    if (x, y) == (0, 1) and vis == t:
        ans += 1

    elif (x, y) != (0, 1) and revision4(mom_c, x, y, vis) and revision5(x, y) and revision6(x, y):

        for i, j in movimientos:

            n_x = i + x
            n_y = j + y
            if revision1(n_x, n_y):
                if revision2(mom_c, vis, x, y):

                    lago[n_x][n_y] = True
                    ice(n_x, n_y, vis + 1, mom_c + 1)
                    lago[n_x][n_y] = False

                elif revision3(mom_c, vis) and revision(x, y, mom_c):

                    lago[n_x][n_y] = True
                    ice(n_x, n_y, vis + 1, mom_c)
                    lago[n_x][n_y] = False

                elif mom_c == 3:

                    lago[n_x][n_y] = True
                    ice(n_x, n_y, vis + 1, mom_c)
                    lago[n_x][n_y] = False


def main():
    n, m = map(int, stdin.readline().split())
    j = 1
    global t
    global ans
    while n != 0 and m != 0:

        for i in range(n):
            lago.append([])
            for _ in range(m):
                lago[i].append(False)

        puntos = list(map(int, stdin.readline().split()))
        puntos_clave.append((puntos[0], puntos[1]))
        puntos_clave.append((puntos[2], puntos[3]))
        puntos_clave.append((puntos[4], puntos[5]))

        ans = 0
        t = n * m
        checks.append(t // 4)
        checks.append(t // 2)
        checks.append((3 * t) // 4)

        # print(checks)

        lago[0][0] = True
        ice(0, 0, 1, 0)

        print(f'Case {j}: {ans}')

        ans = 0
        j += 1
        lago.clear()
        checks.clear()
        puntos_clave.clear()
        n, m = map(int, stdin.readline().split())

    return 0


main()