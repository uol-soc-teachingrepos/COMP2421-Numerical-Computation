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


def plot_covid_cases():
    plt.clf()

    from datetime import datetime
    from scipy.signal import savgol_filter

    N = 31

    def day_number(x):
        date = datetime.strptime(x, "%Y-%m-%d")
        delta = date - datetime.strptime("2020-02-01", "%Y-%m-%d")
        return float(delta.days) / N

    with open("covid-cases.csv") as f:
        data = np.array(
            [
                [day_number(line.split(",")[3]), np.log10(float(line.split(",")[4]))]
                for line in f.readlines()[1:]
            ]
        )

        day = data.T[0]
        cases = data.T[1]

        t = day
        y = savgol_filter(cases, N, 3)

    plt.plot(day, cases, ".", label="data", color="0.75")
    plt.plot(t, y, label="function")
    plt.legend()
    plt.tight_layout()
    plt.savefig("covid-cases-a.svg")

    y_diff = np.gradient(y) / np.gradient(t)
    y_diff = savgol_filter(y_diff, N, 3)
    plt.plot(t, y_diff, label="derivative")

    plt.legend()
    plt.tight_layout()
    plt.savefig("covid-cases-b.svg")

    plt.xticks(
        [
            day_number("2020-02-01"),
            day_number("2020-08-01"),
            day_number("2021-02-01"),
            day_number("2021-08-01"),
        ],
        ["Feb 2020", "Aug 2020", "Feb 2021", "Aug 2021"],
    )
    plt.tight_layout()
    plt.savefig("covid-cases-c.svg")


if __name__ == "__main__":
    plt.rcParams["font.size"] = "16"

    # plot(f1, df1)
    # plot(f2, df2)
    # plot(f3, df3)
    # plot(f4, df4)

    plot_covid_cases()
