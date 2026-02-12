from sys import stdin


def calculate_margin(t, r, tramposo_running, tramposo_cycling, oponentes):
    k = t - r
    # Tiempo del tramposo: T = r/v_r + k/v_k
    tiempo_tramposo = (r / tramposo_running) + (k / tramposo_cycling)

    # Buscamos al oponente más rápido para esta r específica
    # (El que tenga el tiempo mínimo)
    mejor_oponenten = float('inf')
    for opp_running, opp_cycling in oponentes:
        t_opp = (r / opp_running) + (k / opp_cycling)
        if t_opp < mejor_oponenten:
            mejor_oponenten = t_opp

    # El margen en segundos es (T_oponente - T_tramposo) * 3600
    return (mejor_oponenten - tiempo_tramposo) * 3600


def solve(l, r, t, tramposo_running, tramposo_cycling, oponentes):
    if (r - l) < 0.00001:
        ans = l

    else:

        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3

        if calculate_margin(t, m1, tramposo_running, tramposo_cycling, oponentes) < calculate_margin(t, m2, tramposo_running, tramposo_cycling, oponentes):
            ans = solve(m1, r, t, tramposo_running, tramposo_cycling, oponentes)
        else:
            ans = solve(l, m2, t, tramposo_running, tramposo_cycling, oponentes)

    return ans

def main():

    t = int(stdin.readline())
    n = int(stdin.readline())

    velocidades = []
    for _ in range(n):
        running, cycling = map(float, stdin.readline().split())
        velocidades.append((running, cycling))

    tramposo_running, tramposo_cycling = velocidades[-1]
    oponentes = velocidades[:-1]

    mejor_running = solve(0, 100, t, tramposo_running, tramposo_cycling, oponentes)

    print(f"{mejor_running:.2f}, {t - mejor_running:.2f}")

    max_margin = calculate_margin(t, mejor_running, tramposo_running, tramposo_cycling, oponentes)

    print(round(max_margin))



main()