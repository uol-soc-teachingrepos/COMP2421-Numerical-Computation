from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt


def week_number(x):
    date = datetime.strptime(x, "%b %y")
    delta = date - datetime.today()
    return float(delta.days // 7)


# get data
with open("weekly-earnings.csv", "r") as f:

    data = np.array(
        [
            [week_number(line.split(",")[0]), float(line.split(",")[1])]
            for line in f.readlines()[1:]
        ]
    )

    weeks = data.T[0]
    earnings = data.T[1]

# form line equations
n = len(weeks)
A_line = np.array([[w, 1] for w in weeks])
b_line = np.array([[e] for e in earnings])

# find best fit line
x_line = np.linalg.solve(A_line.T @ A_line, A_line.T @ b_line)
print(f"line best fit is y = {x_line[0]} t + {x_line[1]}")

# form quadratic equations
A_quad = np.array([[1, w, w * w] for w in weeks])
b_quad = np.array([[e] for e in earnings])

# find best quadratic fit
x_quad = np.linalg.solve(A_quad.T @ A_quad, A_quad.T @ b_quad)
print(f"quadratic best fit is y = {x_quad[0]} + {x_quad[1]} * t + {x_quad[2]} * t**2")

# plotting options
plt.rcParams["font.size"] = "16"
plt.rcParams["lines.linewidth"] = "3"
# labels
plt.xticks(
    [week_number(f"Jan {year:02d}") for year in range(0, 22, 4)],
    [str(2000 + year) for year in range(0, 22, 4)],
)
plt.xlabel("date")
plt.ylabel("mean weekly earning (£)")

# plot raw
plt.plot(weeks, earnings, ".", label="data")
plt.legend()

# save
plt.tight_layout()
plt.savefig("data.svg")

# plot best fit line
y_line = A_line @ x_line
plt.plot(weeks, y_line, label="line fit")
plt.legend()

# save
plt.tight_layout()
plt.savefig("data-line.svg")

# plot best fit line
y_quad = A_quad @ x_quad
plt.plot(weeks, y_quad, label="quadratic fit")
plt.legend()

# save
plt.tight_layout()
plt.savefig("data-quad.svg")
