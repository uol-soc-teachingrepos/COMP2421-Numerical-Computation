import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import lognorm


def f2(t):
    return np.log(t + 1) * np.exp(-(t ** 2))


def df2(t):
    return np.exp(-(t ** 2)) / (t + 1) - 2 * t * np.log(t + 1) * np.exp(-(t ** 2))


def f3(t):
    return t ** 3 - 2 * t + 2


def df3(t):
    return 3 * t ** 2 - 2


def newton_construction(f, df, iter, filename, trange):
    plt.clf()
    _, ax = plt.subplots()
    ax.axhline(0, color="gray", linewidth=1)

    # plot curve
    t = np.linspace(trange[0], trange[1], 1000)
    ax.plot(t, f(t))

    ylim = [0, 0]

    t0 = 1.0
    ticks = []
    ticklabels = []

    for i in range(iter):
        p0 = ax.plot([t0, t0], [ylim[0], f(t0)], "o-")
        ticks.append(t0)
        ticklabels.append(r"$x^{(" + str(i) + ")}$")

        t1 = t0 - f(t0) / df(t0)
        p1 = ax.plot([t0, t1], [f(t0), 0], "--", color=p0[0].get_color())
        t0 = t1

    plt.xticks(ticks, ticklabels)
    plt.savefig(filename)


if __name__ == "__main__":
    plt.rcParams["font.size"] = "16"

    newton_construction(f2, df2, 5, "newton-2.svg", [0, 3])
    newton_construction(f3, df3, 2, "newton-3.svg", [-0.5, 1.5])
