import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mindrove.board_shim import BoardShim, MindRoveInputParams, BoardIds

# from mindrove.data_filter import DataFilter, FilterTypes, AggOperations


class emg:
    def __init__(self):
        params = MindRoveInputParams()
        self.board_id = BoardIds.MINDROVE_WIFI_BOARD
        self.board_shim = BoardShim(self.board_id, params)

    def record(self, period):
        print("emg start")
        self.board_shim.prepare_session()
        self.board_shim.start_stream()

        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)

        time.sleep(period)

        num_points = period * self.sampling_rate
        self.data = self.board_shim.get_current_board_data(num_points)

        self.board_shim.stop_stream()
        self.board_shim.release_session()
        print("emg done")

    def get_EEG(self):
        eeg_channels = BoardShim.get_eeg_channels(self.board_id)
        return self.data[eeg_channels]
        # df = pd.DataFrame(data)
        # df.to_csv("eeg_data.csv", index=False)

    def get_acceleration(self):
        eeg_channels = BoardShim.get_eeg_channels(self.board_id)
        return self.data[eeg_channels]
        # df = pd.DataFrame(data)
        # df.to_csv("eeg_data.csv", index=False)

    def get_timestamp(self):
        timeStamp = BoardShim.get_timestamp_channel(self.board_id)
        return self.data[timeStamp]

    def get_battery(self):
        battery = BoardShim.get_battery_channel(self.board_id)
        return self.data[battery]

    def plot_data(self):
        df = pd.DataFrame(self.get_EEG())  # Corrected function call

        # Create a single figure with subplots
        fig, axes = plt.subplots(8, 1, figsize=(25, 18))

        for row in range(0, 8):
            data = []
            for x in range(df.shape[1]):
                data.append(df.iloc[row, x])

            axes[row].plot(data)  # Use the respective subplot for each row
            axes[row].set_title(f"Channel {row + 1}")

        plt.show()  # Show the plot after all data has been plotted
