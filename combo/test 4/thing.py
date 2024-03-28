import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

df = pd.read_csv("data/data_emg.csv")
# Create a single figure with subplots
data_list = []
for x in range(df.shape[1]):
    data_list.append(df.iloc[2, x])


# Assuming data_list is your list of data
# data_list = [1, 3, 5, 7, 9, 11, 13, 15]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(40, 6))
(line,) = ax.plot([], [], "b-")


# Function to initialize the plot
def init():
    ax.set_xlim(0, len(data_list))
    ax.set_ylim(0, max(data_list) + 1)
    return (line,)


# Function to update the plot
def update(frame):
    if frame < len(data_list):
        x = np.arange(0, frame + 1)
        y = data_list[: frame + 1]
        line.set_data(x, y)
    return (line,)


# Create animation
ani = FuncAnimation(
    fig, update, frames=len(data_list) + 1, init_func=init, blit=True, interval=0.000002
)

plt.show()

# # # Save animation as GIF
# # ani.save('live_plot.gif', writer='pillow', fps = None)
# fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# v02 = 5
# z2 = g * t**2 / 2 + v02 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f"v0 = {v0} m/s")
# line2 = ax.plot(t[0], z2[0], label=f"v0 = {v02} m/s")[0]
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel="Time [s]", ylabel="Z [m]")
# ax.legend()


# def update(frame):
#     # for each frame, update the data stored on each artist.
#     x = t[:frame]
#     y = z[:frame]
#     # update the scatter plot:
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     # update the line plot:
#     line2.set_xdata(t[:frame])
#     line2.set_ydata(z2[:frame])
#     return (scat, line2)


# ani = FuncAnimation(fig=fig, func=update, frames=40, interval=2)
# plt.show()
