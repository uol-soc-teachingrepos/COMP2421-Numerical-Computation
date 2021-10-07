import numpy as np
from matplotlib import pyplot as plt


def f(t):
    return 1 - np.cos(2.0 * np.pi * t)


for n in range(15):
    plt.clf()

    t = np.linspace(0, 1)
    y = f(t)

    plt.plot(t, y)

    t0 = 0.5
    dt = 0.4 * 2 ** -n

    plt.plot([t0, t0 + dt], [f(t0), f(t0 + dt)])

    plt.plot([t0, t0, 0], [0, f(t0), f(t0)], "--")
    plt.plot([t0 + dt, t0 + dt, 0], [0, f(t0 + dt), f(t0 + dt)], "--")

    plt.xticks([t0, t0 + dt], [r"$t$", r"$t + \mathrm{d}t$"])
    plt.yticks([f(t0), f(t0 + dt)], [r"$y(t)$", r"$y(t + \mathrm{d}t)$"])

    slope = (f(t0 + dt) - f(t0)) / dt
    plt.title(f"Slope = {slope}")
    print(f"Slope = {slope}")

    plt.tight_layout()
    plt.savefig(f"curve-{n}.svg")
