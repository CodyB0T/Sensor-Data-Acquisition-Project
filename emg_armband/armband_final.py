import argparse
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import mindrove
from mindrove.board_shim import BoardShim, MindRoveInputParams, BoardIds
from mindrove.data_filter import DataFilter, FilterTypes, AggOperations


def main():
    period = 5  # time to record in seconds
    fileName = "data.csv"

    BoardShim.enable_dev_board_logger()
    params = MindRoveInputParams()
    board_id = BoardIds.MINDROVE_WIFI_BOARD
    board_shim = BoardShim(board_id, params)

    board_shim.prepare_session()
    board_shim.start_stream()

    eeg_channels = BoardShim.get_eeg_channels(board_id)
    accel_channels = BoardShim.get_accel_channels(board_id)
    sampling_rate = BoardShim.get_sampling_rate(board_id)

    time.sleep(period)

    num_points = period * sampling_rate
    data = board_shim.get_current_board_data(num_points)

    board_shim.stop_stream()
    board_shim.release_session()

    eeg_data = data[eeg_channels]
    accel_data = data[accel_channels]  # output of shape (3, num_of_samples)

    print(eeg_data)
    print(sampling_rate)

    df = pd.DataFrame(eeg_data)
    df.to_csv(fileName, index=False)

    df = pd.read_csv(fileName)

    ####### plot the data #######

    # Create a single figure with subplots
    fig, axes = plt.subplots(8, 1, figsize=(20, 14))

    for row in range(0, 8):
        data = []
        for x in range(df.shape[1]):
            data.append(df.iloc[row, x])

        axes[row].plot(data)  # Use the respective subplot for each row
        axes[row].set_title(f"Channel {row + 1}")

    plt.show()


if __name__ == "__main__":
    main()
