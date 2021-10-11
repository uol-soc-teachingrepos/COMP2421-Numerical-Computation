import numpy as np
from matplotlib import pyplot as plt


def plot(func, dfunc):
    plt.clf()

    x = np.linspace(0, 1, 1000)
    f = func(x)
    df = dfunc(x)

    plt.xlim(min(x), max(x))
    ylim = min(min(f), min(df)), max(max(f), max(df))
    plt.ylim(ylim[0] - 0.1 * (ylim[1] - ylim[0]), ylim[1] + 0.1 * (ylim[1] - ylim[0]))

    plt.plot(x, f, label="function")
    plt.legend()
    plt.savefig(f"{func.__name__}-a.svg")

    plt.plot(x, df, label="derivative")
    plt.legend()
    plt.savefig(f"{func.__name__}-b.svg")


def f1(x):
    return x * (1.0 - x)


def df1(x):
    return 1.0 - 2.0 * x


def f2(x):
    return 1.0 - x ** 4 / 4.0


def df2(x):
    return -(x ** 3)


def f3(x):
    if type(x) == np.ndarray:
        return np.array([f3(xx) for xx in x])

    if x < 0.4:
        return x
    if x > 0.6:
        return 1 - x
    return -5 * x ** 2 + 5 * x - 0.8


def df3(x):
    if type(x) == np.ndarray:
        return np.array([df3(xx) for xx in x])

    if x < 0.4:
        return 1
    if x > 0.6:
        return -1
    return -10 * x + 5


def f4(x):
    if type(x) == np.ndarray:
        return np.array([f4(xx) for xx in x])

    if x < 1.0e-8 or x > 1 - 1.0e-8:
        return 0
    return np.exp(-1 / (x * (1 - x))) * 13


def df4(x):
    if type(x) == np.ndarray:
        return np.array([df4(xx) for xx in x])

    if x < 1.0e-8 or x > 1 - 1.0e-8:
        return 0

    return (
        (-1 / (x * (1 - x) ** 2) + 1 / (x ** 2 * (1 - x)))
        * np.exp(-1 / (x * (1 - x)))
        * 13
    )


if __name__ == "__main__":
    plt.rcParams["font.size"] = "16"

    plot(f1, df1)
    plot(f2, df2)
    plot(f3, df3)
    plot(f4, df4)
