import threading
import time
import pandas as pd

from objects.clarius import clarius
from objects.emg import emg

period = 5  # length in seconds to record, max 10-20 sec

emg = emg()
clar = clarius()

emg_thread = threading.Thread(target=emg.record, args=(period,))
clar_thread = threading.Thread(target=clar.record, args=(period,))

time.sleep(3)  # wait for the deiveces to connect

emg_thread.start()
clar_thread.start()

emg_thread.join()
clar_thread.join()

# clar save data in the c++ code
pd.DataFrame(emg.get_EEG()).to_csv("data/data_emg.csv", index=False)

clar.quit()
