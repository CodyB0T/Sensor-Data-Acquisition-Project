from EMG import EMG
import pandas as pd

emg = EMG()
emg.record(5)

# save eeg data to data.csv
pd.DataFrame(emg.get_EEG()).to_csv("data.csv", index=False)
