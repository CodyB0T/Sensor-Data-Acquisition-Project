import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Create a single figure with subplots
fig, axes = plt.subplots(8, 1, figsize=(20, 14))  # Create 7 subplots in a single column

for row in range(0, 8):
    data = []
    for x in range(df.shape[1]):
        data.append(df.iloc[row, x])

    axes[row].plot(data)  # Use the respective subplot for each row
    axes[row].set_title(f"Channel {row + 1}")

plt.tight_layout()  # Adjusts spacing between subplots
plt.show()
