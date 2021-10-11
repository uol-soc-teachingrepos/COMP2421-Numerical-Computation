import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["font.size"] = "16"

t = np.linspace(0, 1, 1000)
y = -(t - 1) * (t + 0.2)

plt.plot(t, y)


plt.title("An object's speed against time")
plt.xlabel("t: time (s)")
plt.ylabel("S(t): speed (m/s)")

plt.tight_layout()
plt.savefig("speed.svg")