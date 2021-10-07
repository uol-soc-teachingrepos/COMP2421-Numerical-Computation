import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.size"] = "16"


def f(t):
    return 1 - np.cos(2.0 * np.pi * t)


for n in range(3):
    plt.clf()

    # curve
    t = np.linspace(0, 1, 1000)
    y = f(t)
    plt.plot(t, y)

    # base point
    t0 = 0.5
    dt = 0.25 * 2 ** -n

    # line
    plt.plot([t0, t0 + dt], [f(t0), f(t0 + dt)])

    plt.plot([t0, t0, 0], [0, f(t0), f(t0)], "--")
    plt.plot([t0 + dt, t0 + dt, 0], [0, f(t0 + dt), f(t0 + dt)], "--")

    plt.xticks([t0, t0 + dt], [r"$t$", r"$t + \mathrm{d}t$"])
    plt.yticks([f(t0), f(t0 + dt)], [r"$y(t)$", r"$y(t + \mathrm{d}t)$"])

    slope = (f(t0 + dt) - f(t0)) / dt
    plt.text(0.7, 1.7, f"slope {slope:.2f}")

    plt.tight_layout()
    plt.savefig(f"curve-{n}.svg")
