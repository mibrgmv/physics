from math import log
import matplotlib.pyplot as pl

Q = -1.6 * 10e-19
M = 9.1 * 10e-31


def calculate_U():
    u_min = 0
    u_max = 10000
    while u_max - u_min > 10e-6:
        U = (u_max + u_min) / 2
        x, y, vx, vy, t = simulate(v, r, R, L, U)
        if x >= L:
            u_min = U
        else:
            u_max = U
    return x, y, vx, vy, t, U


def simulate(v, r1, r2, l, U):
    x, y = 0, (r2 - r1) / 2 + r1
    v_x, v_y = v, 0
    t, dt = 0, 10e-12
    while x < l and y > r1:
        dvy = (Q * U) / (y * M * log(r2/r1))
        v_y += dvy * dt
        y += v_y * dt
        x += v_x * dt
        t += dt

    return x, y, v_x, v_y, t


def graph(v, r1, r2, l, U):
    x, y = 0, (r2 - r1) / 2 + r1
    vx, vy = v, 0
    t, dt = 0, 10e-12
    yx_data, vy_data, ay_data, yt_data = [], [], [], []
    while x < l or y > r1:
        yx_data.append((x, y))
        vy_data.append((t, vy))
        dvy = (Q * U) / (y * M * log(r2/r1))
        ay_data.append((t, dvy))
        yt_data.append((t, y))
        vy += dvy * dt
        y += vy * dt
        x += vx * dt
        t += dt

    return yx_data, vy_data, ay_data, yt_data


def draw_graph(data: list, title: str, xlabel: str, ylabel: str):
    pl.figure(figsize=(8, 4))
    pl.title(title)
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.plot([i[0] for i in data], [i[1] for i in data])
    pl.grid()
    pl.show()


v = 5.5 * 10e6
r = 0.045
R = 0.1
L = 0.18

x, y, vx, vy, t, U = calculate_U()
yx, vy_list, ay_list, yt = graph(v, r, R, L, U)

print("Минимальное напряжение", U)
print("Время полета", t)
print("Конечная скорость электрона", pow(vy**2 + vx**2, 0.5))

draw_graph(yx, '$y(x)$', '$x$, м', '$y$, м')
draw_graph(vy_list, '$V_y(t)$', '$t$, с', '$V_y$, м/с')
draw_graph(ay_list, '$a_y(t)$', '$t$, с', '$a_y, м/с^2$')
draw_graph(yt, '$y(t)$', '$t$, с', '$y$, м')
