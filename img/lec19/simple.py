import numpy as np
from matplotlib import pyplot as plt

# plotting options
plt.rcParams["font.size"] = "16"
plt.rcParams["lines.linewidth"] = "3"

# line case
plt.clf()

# data
t_line = np.array([1.0, 2.0, 3.0, 4.0])
y_line = np.array([1.0, 1.5, 2.5, 3.5])

plt.plot(t_line, y_line, "o")
plt.tight_layout()
plt.savefig("line-points.svg")

# quad case
plt.clf()

# data
t_quad = np.array([-1, -0.5, 0, 0.5, 1])
y_quad = np.array([1.0, 0.5, 0.0, 0.5, 2.0])

plt.plot(t_quad, y_quad, "o")
plt.tight_layout()
plt.savefig("quad-points.svg")

# Insert an example 5x3 matrix from the overdetermined system.
A = np.array(
    [
        [1.0, -1.0, 1.0],
        [1.0, -0.5, 0.25],
        [1.0, 0.0, 0.0],
        [1.0, 0.5, 0.25],
        [1.0, 1.0, 1.0],
    ]
)

# Insert an example column 5-vector for the right hand side.
b = np.array([[1.0], [0.5], [0.0], [0.5], [2.0]])

x = np.linalg.solve(A.T @ A, A.T @ b)

t = np.linspace(-1, 1, 1000)
y_fit = x[0][0] + x[1][0] * t + x[2][0] * t * t

plt.plot(t, y_fit)
plt.tight_layout()
plt.savefig("quad-lines.svg")
