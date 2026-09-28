import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

log = pd.read_csv("lm35dz_log_1.csv")

fig, ax = plt.subplots()

ax.plot(log["time"], log["temperature"])
ax.hlines(log["temperature"].mean(), log["time"].min(), log["time"].max(), label="Average", color="#C4690E", linestyles="--")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (C)")
ax.set_title("Temperature against Time Measured by LM35DZ Sensor")

ax.legend()
ax.grid()

plt.savefig("lm35dz_plot_1.png")

plt.show()