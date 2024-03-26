from EMG import EMG
from clarius import Clarius
import pandas as pd
import time

clarius = Clarius()

time.sleep(3)

clarius.clarius_timer(5)

clarius.quit()


# emg = EMG()
# emg.record(5)

# # save eeg data to data.csv
# pd.DataFrame(emg.get_EEG()).to_csv("data.csv", index=False)
