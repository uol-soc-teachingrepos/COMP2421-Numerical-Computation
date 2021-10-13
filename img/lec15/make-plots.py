import numpy as np
from matplotlib import pyplot as plt


def wing():
    def y(x):
        return (
            0.2969 * np.sqrt(x)
            - 0.126 * x
            - 0.3516 * x ** 2
            + 0.2843 * x ** 3
            - 0.1015 * x ** 4
        )

    t = np.linspace(0, 1, 1000)

    plt.clf()
    _, ax = plt.subplots()
    ax.axvline(0, color="gray", linewidth=1)
    ax.axhline(0, color="gray", linewidth=1)
    ax.axhline(0.05, linestyle="--", color="gray", linewidth=1)
    ax.axhline(-0.05, linestyle="--", color="gray", linewidth=1)
    p = ax.plot(t, y(t))
    ax.plot(t, -y(t), color=p[0].get_color())

    plt.axis("equal")
    plt.savefig("wing.svg")


def root_example():
    def f(x):
        return x ** 3

    t = np.linspace(-1, 1, 1000)

    plt.clf()
    _, ax = plt.subplots()
    ax.axvline(0, color="gray", linewidth=1)
    ax.axhline(0, color="gray", linewidth=1)
    ax.plot(t, f(t))
    plt.savefig("root-example.svg")


def root_example2():
    def f(x):
        return (x - 0.2) ** 2

    t = np.linspace(-1, 1, 1000)

    plt.clf()
    _, ax = plt.subplots()
    ax.axvline(0, color="gray", linewidth=1)
    ax.axhline(0, color="gray", linewidth=1)
    ax.plot(t, f(t))
    plt.savefig("root-example2.svg")


def newton_construction():
    plt.clf()
    _, ax = plt.subplots()
    ax.axhline(0, color="gray", linewidth=1)

    def f(t):
        return t ** 2 - 0.2

    def df(t):
        return 2 * t

    # plot curve
    t = np.linspace(0, 1)
    ax.plot(t, f(t))

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # plot function evalution
    t0 = 0.8
    p0 = ax.plot([t0, t0, xlim[0]], [ylim[0], f(t0), f(t0)], "o--")

    # plot derivative curve
    p = ax.plot(t, (t - t0) * df(t0) + f(t0))
    ax.text(
        t0 + 0.02,
        f(t0) - 0.02,
        r"slope $f'(x^{(0)})$",
        color=p[0].get_color(),
        rotation=50,
    )

    # plot new function evalution
    t1 = t0 - f(t0) / df(t0)
    ax.plot([t1, t1, xlim[0]], [ylim[0], f(t1), f(t1)], "o--")

    plt.xticks([t0, t1], [r"$x^{(0)}$", r"$x^{(1)}$"])
    plt.yticks([0, f(t0), f(t1)], [r"$0$", r"$f(x^{(0)})$", r"$f(x^{(1)})$"])

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    plt.savefig("newton-graph.svg")


if __name__ == "__main__":
    plt.rcParams["font.size"] = "16"

    wing()
    root_example()
    root_example2()
    newton_construction()
