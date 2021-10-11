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
    return x * x


def df1(x):
    return 2 * x


if __name__ == "__main__":
    plt.rcParams["font.size"] = "16"

    plot(f1, df1)
